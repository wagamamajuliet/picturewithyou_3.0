from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "picturewithyou.users"
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        from .signals import user_signed_up
        # try:
        #     import users.signals  # noqa F401
        # except ImportError:
        #     pass
