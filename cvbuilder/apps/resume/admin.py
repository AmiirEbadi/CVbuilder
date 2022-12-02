from django.contrib import admin
from apps.resume.models import (
    Resume,
    Template,
    Language,
    Education,
    WorkExprience,
    Ability
)

# Register your models here.

@admin.register(Resume)
class AdminResume(admin.ModelAdmin):
    pass

@admin.register(Template)
class AdminTemplate(admin.ModelAdmin):
    pass

@admin.register(Language)
class AdminLanguage(admin.ModelAdmin):
    pass

@admin.register(Education)
class AdminEducation(admin.ModelAdmin):
    pass

@admin.register(WorkExprience)
class AdminWorkExprience(admin.ModelAdmin):
    pass

@admin.register(Ability)
class AdminAbility(admin.ModelAdmin):
    pass