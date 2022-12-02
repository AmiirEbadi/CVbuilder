from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.account.models import User
from apps.resume.models import Resume, Template

@receiver(post_save, sender=User)
def createUserResume(sender, instance, created, **kwargs):
    if created:
        template = Template.objects.get(name='default')
        Resume.objects.create(name=instance, template_id=template.id)