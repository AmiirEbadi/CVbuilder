from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name="نام",
    )
    last_name = models.CharField(
        max_length=200, 
        verbose_name="نام خانوادگی",
    )
    phone = models.CharField(
        max_length=11, 
        default=0,
        blank=False,
        verbose_name="شماره تلفن",
    )
    image = models.ImageField(
        upload_to='images',
        blank=True
    )
    city = models.CharField(
        max_length=200,
        default='tehran',
        blank=False,
        verbose_name="شهر",
    )
    is_complete = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    ) 
    email = models.EmailField(
        blank=False,
        verbose_name="ایمیل",
    )
    about_me = models.TextField(
        blank=False,
        verbose_name="درباره من",
        )
    github = models.URLField(
        default=' ',
        blank=True,
        verbose_name="گیتهاب",
        )
    linkedin = models.URLField(
        default=' ',
        blank=True,
        verbose_name="لینکدین",
        )
    website = models.URLField(
        default=' ',
        blank=True,
        verbose_name="وبسایت",
        )
