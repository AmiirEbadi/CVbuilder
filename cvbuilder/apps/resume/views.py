from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from apps.resume.mixins import ProfileCompletionMixin
from django.shortcuts import (
    render,
    HttpResponse, 
    get_object_or_404, 
    redirect
)
from apps.resume.forms import (
    AddLanguageForm, 
    DeleteForm, 
    AddAbilityForm, 
    AddWorkExperienceForm, 
    AddEducationForm
)
from apps.resume.models import (
    Resume,
    Language,
    Ability,
    Education,
    WorkExprience
)
from django.views.generic.base import (
    TemplateView,
    View,
)

# Create your views here.

class IndexPageView(TemplateView):
    '''
    this view renders a template
    '''
    template_name = 'blog/index.html'


class AddLanguageView(LoginRequiredMixin, ProfileCompletionMixin, CreateView):
    '''
    user can add language with this view
    '''

    success_url = reverse_lazy('resume:add_language')
    template_name = 'blog/add-language.html'
    form_class = AddLanguageForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_resume = Resume.objects.get(name=self.request.user)
        user_languages = Language.objects.filter(resume=user_resume)
        context['list_of_languages'] = user_languages
        return context


class DeleteLanguageView(View):
    '''
    User send request to this view for deleting
    an object
    '''
    form_class = DeleteForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            object_id = form.cleaned_data['id']
            user_resume = get_object_or_404(Resume,name=request.user)
            user_language = user_resume.related_language.get(id=object_id).delete()

        return redirect('resume:add_language')

        
class DeleteAbilityView(View):
    '''
    User send request to this view for deleting
    an object
    '''
    form_class = DeleteForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            object_id = form.cleaned_data['id']
            user_resume = get_object_or_404(Resume,name=request.user)
            user_ability = user_resume.related_ability.get(id=object_id).delete()

        return redirect('resume:add_ability')


class AddAbilityView(LoginRequiredMixin, ProfileCompletionMixin, CreateView):
    '''
    user can add ability with this view
    '''
    success_url = reverse_lazy('resume:add_ability')
    template_name = 'blog/add-ability.html'
    form_class = AddAbilityForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user_resume = Resume.objects.get(name=self.request.user)
        user_abilities = Ability.objects.filter(resume=user_resume)
        context['list_user_abilities'] = user_abilities
        return context


class AddWorkExprienceView(LoginRequiredMixin, ProfileCompletionMixin, CreateView):
    '''
    user can add work experiences with this view
    '''
    form_class = AddWorkExperienceForm
    success_url = reverse_lazy('resume:add_work_experience')
    template_name = 'blog/add-work-experience.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user_resume = Resume.objects.get(name=self.request.user)
        user_work_exp = WorkExprience.objects.filter(resume=user_resume)
        context['list_user_work_experience'] = user_work_exp
        return context


class DeleteWorkExperienceView(View):
    '''
    User send request to this view for deleting
    an object
    '''
    form_class = DeleteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            object_id = form.cleaned_data['id']
            user_resume = Resume.objects.get(name=request.user)
            user_work_experience = user_resume.related_work.get(id=object_id).delete()
        return redirect('resume:add_work_experience')


class AddEducationView(LoginRequiredMixin, ProfileCompletionMixin, CreateView):
    '''
    user can add education with this view
    '''
    form_class = AddEducationForm
    template_name = 'blog/add-education.html'
    success_url = reverse_lazy('resume:add_education')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user_resume = Resume.objects.get(name=self.request.user)
        user_education = Education.objects.filter(resume=user_resume)
        context['list_user_education'] = user_education
        return context


class DeleteEducationView(View):
    '''
    User send request to this view for deleting
    an object
    '''
    form_class = DeleteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            object_id = form.cleaned_data['id']
            user_resume = Resume.objects.get(name=request.user)
            user_education = user_resume.related_education.get(id=object_id).delete()
        return redirect('resume:add_education')




class ResumeView(LoginRequiredMixin, ProfileCompletionMixin, TemplateView):
    '''
    this view displays user resume
    '''

    template_name = 'resume_template/default.html'

    def get_context_data(self, **kwargs):
        print("hi")
        context = super().get_context_data()
        user_resume = Resume.objects.get(name=self.request.user)
        context['resume'] = user_resume
        context['languages'] = Language.objects.filter(resume=user_resume)
        context['work_experiences'] = WorkExprience.objects.filter(resume=user_resume)
        context['abilities'] = Ability.objects.filter(resume=user_resume)
        context['educations'] = Education.objects.filter(resume=user_resume)
        return context





