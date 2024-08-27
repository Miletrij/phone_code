from django.contrib.auth.models import AbstractBaseUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractBaseUser):
    username = None
    password = None
    phone = models.CharField(unique=True, max_length=12, verbose_name="Телефон",
                             help_text="Введите номер телефона")
    phone_code = models.CharField(max_length=4, verbose_name="код авторизации",)
    invite_code = models.CharField(max_length=6, verbose_name="код приглашения", **NULLABLE)
    invite_pole = models.TextField(max_length=6, verbose_name="поле для приглашения", **NULLABLE)
    USERNAME_FIELD = "phone"
    PASSWORD_FIELD = "phone_code"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone} {self.phone_code}'

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
