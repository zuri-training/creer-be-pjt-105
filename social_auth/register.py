from django.contrib.auth import authenticate
from authentication.models import User
from environs import Env

import random
from rest_framework.exceptions import AuthenticationFailed

env = Env()
env.read_env()


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return random_username


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email.auth_provider:
            registered_user = authenticate(
                email=email, password=env.str("SOCIAL_SECRET"))
            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'token': registered_user.token
            }

        else:
            raise AuthenticationFailed(
                'Please continue your login using' + str(filtered_user_by_email[0].auth_provider['creer']))

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': env.str('SOCIAL_SECRET')
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        new_user = authenticate(
            email=email, password=env.str('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'token': new_user.token,
        }
