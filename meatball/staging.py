from django.http import HttpResponse
from django.conf import settings
import base64


class BasicAuthMiddleware():

    def unauthed(self):
        response = HttpResponse('''<html><title>Auth required</title><body>
                                <h1>Authorization Required</h1></body></html>''', content_type='text/html')
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        response.status_code = 401
        return response

    def process_request(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return self.unauthed()
        else:
            authentication = request.META['HTTP_AUTHORIZATION']
            (authmeth, auth) = authentication.split(' ', 1)
            if 'basic' != authmeth.lower():
                return self.unauthed()
            auth = auth.strip()
            auth = base64.b64decode(auth.encode())
            try:
                auth = auth.decode()
            except UnicodeDecodeError:
                return self.unauthed()
            try:
                username, password = auth.split(':', 1)
            except ValueError:
                return self.unauthed()
            if username == settings.BASICAUTH_USERNAME and password == settings.BASICAUTH_PASSWORD:
                return None

            return self.unauthed()
