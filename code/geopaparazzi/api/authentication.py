from django.contrib.auth.models import AnonymousUser
from oauth2_provider.models import AccessToken
from tastypie.authentication import Authentication

from geopaparazzi.api.views import verify_access_token
from geopaparazzi.base.auth import get_token_from_auth_header


class OAuthAuthentication(Authentication):

    def extract_auth_header(self, request):
        auth_header = None
        try:
            auth_header = request.META.get(
                'HTTP_AUTHORIZATION', request.META.get('HTTP_AUTHORIZATION2'))
        except KeyError:
            pass
        return auth_header

    def token_is_valid(self, token):
        valid = False
        try:
            verify_access_token(None, token)
            valid = True
        except Exception:
            pass
        return valid

    def is_authenticated(self, request, **kwargs):
        user = AnonymousUser()
        authenticated = False
        if 'HTTP_AUTHORIZATION' in request.META:
            auth_header = self.extract_auth_header(request)
            if auth_header:
                access_token = get_token_from_auth_header(auth_header)
                if self.token_is_valid(access_token):
                    obj = AccessToken.objects.get(token=access_token)
                    user = obj.user
                    authenticated = True
        request.user = user
        return authenticated
