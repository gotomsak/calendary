from .models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = (
        #
        #     'id',
        #     'email',
        #     'password',
        #     'image',
        #     'status',
        # )


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"


class SignUpSerializer(serializers.ModelSerializer):
    # passwordを返さないようにした
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]

        return User.objects.create_user(username=username, email=email, password=password)



