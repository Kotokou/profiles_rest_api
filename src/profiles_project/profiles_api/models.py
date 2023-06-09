from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""
    def create_user(self, email, name, password=None):
        """Let create and save user"""
        if not email:
            raise ValueError("User must have email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Let create and save superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents 'User profile ' in our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Use to get user full name"""
        return self.name

    def get_short_name(self):
        """Use to get user short name"""
        return self.name

    def __str__(self):
        """Use to convert objects to strings"""
        return self.email
