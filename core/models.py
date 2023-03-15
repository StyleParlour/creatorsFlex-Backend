from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class SocialLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class ContentType(models.Model):
    contentName = models.CharField(max_length=255)

    def __str__(self):
        return self.contentName

class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(null=True, blank=True, upload_to='content')
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    caption = models.CharField(null=True, blank=True, max_length=255)
    hashTags = models.CharField(null=True, blank=True, max_length=255)
    uploadAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    uploadToAccount = models.ForeignKey(SocialLogin, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class ContactDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def  __str__(self):
        return self.name
