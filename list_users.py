import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from users.models import User

def main():
    users = User.objects.all()
    if not users:
        print("Пользователей нет.")
    else:
        print("Список email пользователей:")
        for u in users:
            print(u.email)

if __name__ == '__main__':
    main()
