import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from core.abstract.models import AbstractManager,AbstractModel

# Create your models here.
class UserManager(BaseUserManager,AbstractManager):

    def create_user(self,username,email,password=None,**kwargs):
        # Create and return a `User` with an email,phone number, username and password
        if username is None:
            raise TypeError("Users must have username.")
        if email is None:
            raise TypeError("Users must have email.")
        if password is None:
            raise TypeError("Users must have password.")
        user = self.model(username=username,email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    #===========# 

    def create_superuser(self,username, email, password=None, **extra_fields):
        """Creates and returns a superuser."""
        if username is None:
            raise TypeError("Superusers must have username.")
        if email is None:
            raise TypeError("Superusers must have email.")
        if password is None:
            raise TypeError("Superusers must have password.")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractModel,AbstractBaseUser,PermissionsMixin):

    username = models.CharField(db_index=True,max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female")],
        blank=True,
        null=True,
        default="male",
    )
    is_verified = models.BooleanField(default=False)  # Email/phone verification
    preferred_language = models.CharField(max_length=10, blank=True, null=True)
    liked_posts = models.ManyToManyField("core_post.Post",related_name="liked_by")
    # Custom fields for user roles
    USER_TYPES = [
        ("admin", "Admin"),
        ("customer", "Customer"),
        ("seller", "Seller"),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default="customer")


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
            return self.username

    def like(self,post):
         return self.liked_posts.add(post)
    def remove_like(self,post):
         return self.liked_posts.remove(post)
    def has_liked(self,post):
         return self.liked_posts.filter(pk=post.pk).exists()
    @property
    def name(self):
            return f"{self.first_name}-{self.last_name}"


