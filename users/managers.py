from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("User Must Have an Email")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.role = "user"
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_email_verified = True
        user.role = "admin"
        user.save(using=self._db)
        return user
