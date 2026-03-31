"""Create admin user for InsightGrid (admin@gmail.com / admin123)."""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create admin user (admin@gmail.com / admin123)"

    def handle(self, *args, **kwargs):
        email = "admin@gmail.com"
        username = "admin"
        password = "admin123"

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"User '{username}' already exists."))
            return

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        self.stdout.write(self.style.SUCCESS(f"Admin user created: {email}"))
