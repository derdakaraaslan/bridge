from ninja import NinjaAPI
from ninja.security import HttpBearer
from rest_framework.authtoken.models import Token

from ..exceptions import (UnauthorizedException, unauthorized_handler)


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            print("************************")
            token_instance = Token.objects.get(key=token)
            
            request.user = token_instance.user
            return token
        except Exception:
            return None
        
api = NinjaAPI(version="1.0.0", auth=AuthBearer())

api.add_exception_handler(UnauthorizedException, unauthorized_handler)