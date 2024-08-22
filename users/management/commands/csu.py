from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(phone="79991234567")
        user.set_password("12345678")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
