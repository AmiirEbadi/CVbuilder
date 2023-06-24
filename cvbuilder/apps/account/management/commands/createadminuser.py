from django.conf import settings
from django.core.management.base import BaseCommand
from apps.account.models import User
from apps.resume.models import Template
class Command(BaseCommand):

    def handle(self, *args, **options):
        t = Template.objects.create(name='default')
        t.save()
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(email="admin@admin.com", username="admin", password="admin")
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            
        else:
            print('Admin accounts can only be initialized if no Accounts exist')