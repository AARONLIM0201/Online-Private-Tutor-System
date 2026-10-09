"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,BaseUserManager

#sharing entity
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,role,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not role:
            raise ValueError("Users must have a role")
        
        user = self.model(
            email = self.normalize_email(email), #normalize_email is a method of BaseUserManager
            username = username,
            role = role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,role,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            role=role,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    ROLE_CHOICES = [
        ('Tutor', 'Tutor'),
        ('Parents', 'Parents'),
        ('Student', 'Student'),
    ]
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=40, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=40) 
    # last_name = models.CharField(max_length=40)
    # phone_number = models.CharField(max_length=40)
    # profile_picture = models.ImageField(null=True, blank=True)
    # bio = models.TextField()
    # hide_email = models.BooleanField(default=True)
    # hide_phone_number = models.BooleanField(default=True)
    # hide_profile_picture = models.BooleanField(default=True)
    # hide_bio = models.BooleanField(default=True)
    # hide_name = models.BooleanField(default=True)
    # hide_last_name = models.BooleanField(default=True)
    # hide_date_joined = models.BooleanField(default=True)
    # hide_last_login = models.BooleanField(default=True)
    # hide_is_admin = models.BooleanField(default=True)
    # hide_is_staff = models.BooleanField(default=True)
    # hide_is_active = models.BooleanField(default=True)
    # hide_is_superuser = models.BooleanField(default=True)
    # hide_password = models.BooleanField(default=True)
    # hide_username = models.BooleanField(default=True)
    # hide_profile = models.BooleanField(default=True)
    # hide_account = models.BooleanField(default=True)
    # hide_user = models.BooleanField(default=True)
    USERNAME_FIELD = 'email' #login criteria
    REQUIRED_FIELDS = ['username','role'] #fields required


    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True