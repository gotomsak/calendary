from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from django.urls import path
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import SignUpSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import status

class TokenView(APIView):

    def get(self, request):

        # 本来は認証しよう

        # user = TokenAuthentication.authenticate(request.query_params['email'], request.query_params['password'])
        user = User.objects.get(email=request.GET['email'])
        check = user.check_password(request.GET['password'])

        if not check:
            raise exceptions.AuthenticationFailed('メールアドレスまたはパスワードが違います')
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': str(token)})


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    #
    # @transaction.atomic
    # def post(self,request):
    #     serializer = SignUpSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post'])
    # def get_signup(self, request):
    #     print(request.data)
    #     user = self.get_object()
    #     print(user)
    #     serializer = SignUpSerializer(data=request.data)
    #     print(serializer)
    #     print(user)
    #     return Response({"nyan": "nyan"})



class UserInfoView(APIView):

    def get(self, request):
        # queryset = User.objects.all()
        # serializer_class = UserInfoSerializer
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        # serializer.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(key=request.META['HTTP_AUTHORIZATION'])

        # user = serializer.validated_data['user']
        # token, _ = Token.objects.get_or_create(user=queryset)
        user = User.objects.get(pk=token.user_id)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
            'pass': user.password
        })

    # def authenticate(self, request):
    #     print(request)
    #     user, auth = super().authenticate(request)
    #     return user, auth


# class ExpirationTokenAuthentication(TokenAuthentication):
#     delta = timezone.timedelta(seconds=10)
#
#     def authenticate(self, request):
#         print(request)
#         user, auth = super().authenticate(request)
#         if timezone.now() - auth.created > self.delta:
#             auth.delete()
#             raise exceptions.AuthenticationFailed('有効期限切れだよ')
#
#         # 毎回有効期限を更新する場合
#         # auth.create = timezone.now()
#         # auth.save()
#         return user, auth
