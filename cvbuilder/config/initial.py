from django.contrib.auth import get_user_model
import apps.resume.models as resume

def initialize():
    default_template = resume.Template.objects.get_or_create(name='default')
    
    
    User = get_user_model()
    
    user = User.objects.filter(username='admin')
    
    if not user:
        print('Creating admin user')
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin')  
    
    
