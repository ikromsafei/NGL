#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin_pengintip').exists():
    User.objects.create_superuser('admin_pengintip', 'admin@example.com', 'PasswordRahasia123')
EOF