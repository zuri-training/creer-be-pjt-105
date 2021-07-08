from google.auth.transport import requests
from google.oauth2 import id_token
# from environ import Env
# import os
# env = Env()
# env.read_env()

class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        try:
            request = requests.Request()
            id_info = id_token.verify_oauth2_token(
                auth_token, request)
            if 'accounts.google.com' in id_info['iss']:
                return id_info 
            
        except:
            return "The token is either invalid or has expired"