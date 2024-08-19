from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    phone = models.CharField(unique=True, max_length=12, verbose_name="Телефон",
                             help_text="Введите номер телефона")
    phone_code = models.CharField(max_length=50, verbose_name="код авторизации", **NULLABLE)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return {self.phone}

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
