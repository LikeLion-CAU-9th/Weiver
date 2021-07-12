from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.expressions import Value
from django.utils import tree

# Create your models here.
class CustomUserManager(BaseUserManager):
    # create_user, create_superuser 를 override해서 modify 해줘야
    def create_user(self, email, nickname, password = None):
        # param으로 USERNAME_FIELD + REQUIRED_FIELD
        if not email: 
            raise ValueError("Users must have an email address")
        if not nickname: 
            raise ValueError("Users must have nickname")

        user = self.model(
            email = self.normalize_email(email), # email을 lowercase
            nickname = nickname,
            # user_thumbnail = user_thumbnail,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email = self.normalize_email(email),
            nickname = nickname,
            password = password,
            # user_thumbnail = None, 
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True        
        user.save(using= self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name= "이메일", 
        max_length=60,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name = "닉네임",
        max_length=10,
        unique= True)
    joined_on = models.DateField(
        verbose_name= "가입일자",
        auto_now_add=True
        )
    # user_thumbnail = models.ImageField(upload_to = "media/", null= True, blank = True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # login에 이용할 field 
    REQUIRED_FIELDS = ['nickname', ]
    # register 시 실제로 fill in 할 attributes 
    # email은 USERNAME_FIELD로 들어갔고, 나머지는 default 값으로 들어감.

    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        # 해당 user에게 permission 여부 
        return self.is_admin
    
    def has_module_perms(self, app_label):
        # no matter what will have module permission
        return True