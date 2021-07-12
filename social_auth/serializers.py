from rest_framework import serializers
from .google import Google
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed
from environs import Env

env = Env()
env.read_env()

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField(allow_blank=False,
    trim_whitespace = True)

    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'Valifation error The token is invalid or expired.Please login again'
            )

        # if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
        #     raise AuthenticationFailed('oops, who are you ?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider = provider, user_id=user_id, email=email, name=name
)
