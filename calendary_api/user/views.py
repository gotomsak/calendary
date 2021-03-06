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
from .serializers import TokenSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import status
from rest_framework import generics
from datetime import timedelta
from rest_framework import mixins


class LoginView(APIView):
    @staticmethod
    def get(request):

        user = User.objects.get(email=request.GET['email'])
        check = user.check_password(request.GET['password'])

        if not check:
            raise exceptions.AuthenticationFailed('パスワードが違います')

        # loginするたびtokenを発行しなおす
        try:
            token = Token.objects.get(user=user)
            Token.objects.filter(key=token).delete()
        except Token.DoesNotExist:
            pass
        token = Token.objects.create(user=user)
        username = user.username
        print(username)
        return Response((UserInfoSerializer(user).data, TokenSerializer(token).data))


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

    @staticmethod
    def delete(request):
        token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'])
        User.objects.filter(pk=token.user_id).delete()
        return Response({'result': 'logoutしました'})


class UserInfoView(APIView):
    # queryset = User.objects.all()
    # serializer_class = User
    @staticmethod
    def get(request):
        # queryset = User.objects.all()
        # serializer_class = UserInfoSerializer
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        # serializer.is_valid(raise_exception=True)
        #token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'])

        try:
            token = Token.objects.get(key=request.GET['token'])
            user = User.objects.get(id=token.user_id)

        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('tokenが違います')

        token.delete()

        token = Token.objects.create(user=user)




        # user = serializer.validated_data['user']
        # token, _ = Token.objects.get_or_create(user=queryset)
        # user = User.objects.get(pk=token.user_id)
        # print(user)
        return Response((UserInfoSerializer(user).data, TokenSerializer(token).data))


class UserEntryView(APIView):

    @staticmethod
    def get(request):
        #print(request)
        user = User.objects.get(email=request.GET['email'])
        check = user.check_password(request.GET['password'])

        if not check:
            raise exceptions.AuthenticationFailed('パスワードが違います')

        # loginするたびtokenを発行しなおす
        try:
            token = Token.objects.get(user=user)
            Token.objects.filter(key=token).delete()
        except Token.DoesNotExist:
            pass
        token = Token.objects.create(user=user)

        username = user.username
        print(username)

        return Response({'token': str(token)})

    @staticmethod
    def post(request):
        print(request)
        user = User.objects.all()
        serializer = SignUpSerializer(user)
