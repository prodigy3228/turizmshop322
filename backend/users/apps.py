from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Импортируем здесь, чтобы избежать ошибки AppRegistryNotReady
        from django.contrib.auth import get_user_model
        
        def create_superuser(sender, **kwargs):
            User = get_user_model()
            username = "admin"
            email = "admin@example.com"
            password = "AdminPass123"  # Замените на свой пароль
            
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
                print(f"✅ Суперпользователь {username} создан!")
            else:
                print(f"✅ Пользователь {username} уже существует.")
        
        # Подключаем функцию к сигналу post_migrate
        post_migrate.connect(create_superuser, sender=self)