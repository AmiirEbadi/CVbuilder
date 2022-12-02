from django.db import models
from apps.account.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


LANGUAGE_ABILITY_LEVEL = (
    (1, 'ضعیف'),
    (2, 'متوسط'),
    (3, 'خوب'),
    (4, 'عالی'),
)


class Template(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.OneToOneField(
        User,
        on_delete=models.CASCADE, 
        null=True,
        verbose_name='نام'       
        )
    template = models.ForeignKey(
        Template, 
        on_delete=models.CASCADE, 
        default='1', 
        null=True
    )

    class Meta:
        verbose_name='resume'
        verbose_name_plural='resumes'

    def __str__(self):
        return self.name.username

class Language(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='عنوان'
    )
    level = models.IntegerField(
        choices=LANGUAGE_ABILITY_LEVEL,
        verbose_name='سطح'
    )
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='related_language'
    )

    class Meta:
        verbose_name='language'
        verbose_name_plural='languages'


    def __str__(self):
        return self.title

class WorkExprience(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان'
        )
    company_name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name='نام شرکت'
        )
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE, 
        related_name='related_work'
    )
    start_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1380),MaxValueValidator(1401)],
        verbose_name='سال شروع'
    )
    start_month = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(12)],
        verbose_name='ماه شروع'

    )
    end_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1380),MaxValueValidator(1401)],
        verbose_name='سال پایان'

    )
    end_month = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(12)],
        verbose_name='ماه پایان'
    )
    description  = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name='work experience'
        verbose_name_plural='work experiences'

    def __str__(self):
        return self.title

class Ability(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان'
        )
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='related_ability'
        )

    class Meta:
        verbose_name='ability'
        verbose_name_plural='abilities'


    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=200)
    university = models.CharField(
        max_length=200,
        blank = True,
        verbose_name = 'نام محل تحصیل'
        )
    start_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1380),MaxValueValidator(1401)],
        verbose_name = 'سال شروع'

    )
    end_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1380),MaxValueValidator(1401)],
        verbose_name = 'سال پایان'

    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        null=True, 
        related_name='related_education'
        )

    class Meta:
        verbose_name='education'
        verbose_name_plural='educations'

    def __str__(self):
        return self.title