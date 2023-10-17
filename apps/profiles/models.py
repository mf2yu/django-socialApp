from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, 
    default="+41524240242")
    bio = models.TextField(verbose_name=_("Bio"), default="say something about yourself")
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), 
    default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, 
    default=Gender.OTHER, max_length=20)
    website = models.URLField(max_length=200)
    country = CountryField(verbose_name=_("Country"), default="US", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="New York", 
    blank=False, null=False)
    num_following =models.IntegerField(verbose_name=_("Following"), default=0, null=True, 
    blank=True)
    num_followers =models.IntegerField(verbose_name=_("Followers"), default=0, null=True, 
    blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    
