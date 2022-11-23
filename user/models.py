from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, username, phone, age, password=None):

        if not email:
            raise ValueError('email must be defined.')
        if not username:
            raise ValueError('username must be defined.')
        
        user = self.model(email = self.normalize_email(email), username = username, phone = phone, age = age)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, phone, age, password=None):

        user = self.create_user(email=email, username=username, phone=phone, age=age, password=password)

        user.is_admin = True
        user.save(using=self._db)

        return user
class User(AbstractBaseUser):

    objects = UserManager()

    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    username = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    phone = models.CharField(default='', max_length=30, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta:

        db_table = 'user'