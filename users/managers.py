from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, requested_phone, verified_phone=None, password=None):
        if not requested_phone:
            raise ValueError("User Must Have a Phone")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            requested_phone=requested_phone,
            verified_phone=verified_phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, requested_phone, verified_phone=None, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            requested_phone=requested_phone,
            verified_phone=verified_phone,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
