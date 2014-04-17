from django.contrib.auth.admin import User

class LoginBackend(object):
    def authenticate(self, username = None):
        try:
           return User.objects.get(email = username)
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id = user_id)
        except:
            return None

