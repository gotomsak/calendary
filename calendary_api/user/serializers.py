from .models import User
from rest_framework import serializers


# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'email',
#
#         )


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = (


            'email',
            'password'
        )

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(email=validated_data["email"],password=validated_data["password"])

