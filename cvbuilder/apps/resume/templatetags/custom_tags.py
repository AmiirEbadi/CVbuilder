from django import template
from apps.resume.models import *

register = template.Library()

@register.inclusion_tag('blog/side-menu.html')
def side_menu(user):
    user = Resume.objects.get(name=user)
    language_count = Language.objects.filter(resume=user).count()
    education_count = Education.objects.filter(resume=user).count()
    work_exp_count = WorkExprience.objects.filter(resume=user).count()
    ability_count = Ability.objects.filter(resume=user).count()

    return {
        'language_count':language_count,
        'education_count':education_count,
        'work_exp_count':work_exp_count,
        'ability_count':ability_count
        }