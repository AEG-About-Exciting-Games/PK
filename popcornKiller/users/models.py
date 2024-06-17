from django.contrib.auth.models import  BaseUserManager, AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        이메일과 비밀번호로 사용자를 생성하고 반환합니다.
        """
        if not email:
            raise ValueError("이메일 필드는 반드시 설정되어야 합니다.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        이메일과 비밀번호로 슈퍼유저를 생성하고 반환합니다.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)

    nickname = models.CharField(max_length=30)

    objects = CustomUserManager()  # 재정의된 매니저 클래스 추가

    USERNAME_FIELD = "email"  # 고유 식별자로 이메일 사용
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []  # 이제 기본적으로 이메일이 필요하므로 이 목록에서 제거
