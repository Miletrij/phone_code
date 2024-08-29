import string
import random

from django.db import models


def generate_invite_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


class User(models.Model):
    phone_number = models.CharField(unique=True, max_length=12, verbose_name="Телефон",
                             help_text="Введите номер телефона")
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code,
                                   verbose_name="код приглашения")
    invite_pole = models.TextField(max_length=6, verbose_name="поле для приглашения", null=True, blank=True)

    def __str__(self):
        return self.phone_number
