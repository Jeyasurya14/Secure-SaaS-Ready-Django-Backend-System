from django.db import migrations
from django.contrib.auth import get_user_model
import os

def create_admin(apps, schema_editor):
    User = get_user_model()
    # Flexible credentials: Read from Env or use Defaults
    email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
    password = os.environ.get('ADMIN_PASSWORD', 'SecurePass123!')
    
    if not User.objects.filter(email=email).exists():
        print(f"DTOOL: Creating superuser {email}")
        User.objects.create_superuser(email=email, password=password, role='admin')
    else:
        print("DTOOL: Superuser already exists")

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
