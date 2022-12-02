from django.urls import path,include
from .views import (
    IndexPageView,
    AddLanguageView,
    AddAbilityView,
    DeleteLanguageView,
    DeleteAbilityView,
    DeleteWorkExperienceView,
    AddWorkExprienceView,
    AddEducationView,
    DeleteEducationView,
    ResumeView
)

app_name = 'resume'


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('add-language/', AddLanguageView.as_view(), name='add_language'),
    path('add-ability/', AddAbilityView.as_view(), name='add_ability'),

    path('remove-language/', DeleteLanguageView.as_view(), name='delete_language'),
    path('remove-ability/', DeleteAbilityView.as_view(), name='delete_ability'),

    path('add-work/', AddWorkExprienceView.as_view(), name='add_work_experience'),
    path('remove-work/', DeleteWorkExperienceView.as_view(), name='delete_work_experience'),

    path('add-education/', AddEducationView.as_view(), name='add_education'),
    path('resume/', ResumeView.as_view(), name='resume'),

    path('remove-education/', DeleteEducationView.as_view(), name='delete_education')

]
