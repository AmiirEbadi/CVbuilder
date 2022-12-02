from django import forms
from apps.resume.models import (
    Language, 
    Resume, 
    Ability,
    WorkExprience,
    Education
)
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError



class AddLanguageForm(forms.ModelForm):
    '''
        this form get the request from kwargs and checks wheather
        the user has the same language
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.user_resume = Resume.objects.get(name=self.request.user)
        super().__init__(*args, **kwargs)

        
    def clean_title(self):
        title = self.cleaned_data['title']
        user_languages = self.user_resume.related_language.filter(title=title)
        if not user_languages:
            return title
        else:
            raise ValidationError('این عنوان برای زبان از قبل برای شما ثبت شده است')

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.resume = self.user_resume
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Language
        fields = ('title','level')



class AddAbilityForm(forms.ModelForm):
    '''
        this form get the request from kwargs and checks wheather
        the user has the same ability
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.user_resume = Resume.objects.get(name=self.request.user)
        super().__init__(*args, **kwargs)

        
    def clean_title(self):
        title = self.cleaned_data['title']
        user_abilites = self.user_resume.related_ability.filter(title=title)
        if not user_abilites:
            return title
        else:
            raise ValidationError('این عنوان برای مهارت از قبل برای شما ثبت شده است')

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.resume = self.user_resume
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Ability
        fields = ('title',)



class AddWorkExperienceForm(forms.ModelForm):
    '''
        this form get the request from kwargs and checks wheather
        the user has the same ability
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.user_resume = Resume.objects.get(name=self.request.user)
        super().__init__(*args, **kwargs)
    
        
    def clean(self):
        start_year = self.cleaned_data['start_year']
        end_year = self.cleaned_data['end_year']

        if start_year > end_year:
            raise ValidationError('سال شروع و پایان کار تطابق ندارد .')
        return self.cleaned_data

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.resume = self.user_resume
        if commit:
            obj.save()
        return obj

    class Meta:
        model = WorkExprience
        fields = (
            'title',
            'company_name',
            'start_year', 
            'start_month',
            'end_year', 
            'end_month',
            'description',
            )





class AddEducationForm(forms.ModelForm):
    '''
       this form get the request from kwargs and
       if the start year of education is greater 
       than end year it raises an error
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.user_resume = Resume.objects.get(name=self.request.user)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.resume = self.user_resume
        if commit:
            obj.save()
        return obj

    def clean(self):
        start_year = self.cleaned_data['start_year']
        end_year = self.cleaned_data['end_year']

        if start_year > end_year:
            raise ValidationError('سال شروع و پایان تحصیل تطابق ندارد.')
        return self.cleaned_data
        
    class Meta:
        model = Education
        fields = (
            'title',
            'university',
            'start_year',
            'end_year'
        )



class DeleteForm(forms.Form):
    '''
    this form get an id of an object for delete stuff
    '''
    id = forms.IntegerField()



