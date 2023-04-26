from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class GeneradorToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.id) + six.text_type(timestamp)) + six.text_type(user.is_active)

token_activacion = GeneradorToken()