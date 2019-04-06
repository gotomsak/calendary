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
from .serializers import UserInfoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import status
from rest_framework import generics
from datetime import timedelta


class LoginView(APIView):

    def get(self, request):

        user = User.objects.get(email=request.GET['email'])
        check = user.check_password(request.GET['password'])

        if not check:
            raise exceptions.AuthenticationFailed('パスワードが違います')

        # loginするたびtokenを発行し直す
        try:
            token = Token.objects.get(user=user)
            Token.objects.filter(key=token).delete()
        except Token.DoesNotExist:
            pass
        token = Token.objects.create(user=user)

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


class LogoutViewSet(APIView):
    def delete(self, request):
        token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'])
        User.objects.filter(pk=token.user_id).delete()
        return Response({'result': 'logoutしました'})


class UserInfoView(APIView):
    # queryset = User.objects.all()
    # serializer_class = User

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
        return Response(UserInfoSerializer(user).data)
        #
        # return Response({
        #     'token': token.key,
        #     'user_id': user.id,
        #     'email': user.email,
        #     'pass': user.password
        # })

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
