
# Create your models here.
from django.db import models
from django.utils.translation import get_language
from django.contrib.auth.models import AbstractUser as AU



class Manual_User(AU):
    pass

class Worker(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    teudat_zeut = models.CharField(max_length=10, default="")
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10, default="")
    vip = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=10, default="")
    city = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=50, default="")
    phone1 = models.CharField(max_length=10, default="")
    phone2 = models.CharField(max_length=10, default="")
    email = models.CharField(max_length=30, default="")
    birth_date = models.CharField(max_length=10, default="")
    reg_date = models.CharField(max_length=10, default="")
    age = models.IntegerField(default=0)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"user_id: {str(self.user_id)}"


class Agent(models.Model):
    affiliate_id = models.CharField(max_length=10)
    affiliate_name = models.CharField(max_length=20, default="")
    parent_company = models.CharField(max_length=20, default="")
    staff_ids = models.CharField(max_length=100, default="")
    affiliate_country = models.CharField(max_length=20, default="")
    affiliate_city = models.CharField(max_length=20, default="")
    affiliate_location = models.CharField(max_length=50, default="")
    affiliate_percent = models.CharField(max_length=2, default="")
    phone1 = models.CharField(max_length=13, default="")
    phone2 = models.CharField(max_length=13, default="")
    email = models.CharField(max_length=30, default="")
    site = models.CharField(max_length=30, default="")
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=15, default="")
    contact_id = models.CharField(max_length=10, default="")
    reg_date = models.CharField(max_length=20, default="")
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.affiliate_id)


class Lead(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=15, default="")
    first_name = models.CharField(max_length=10, default="")
    last_name = models.CharField(max_length=10, default="")
    teudat_zeut = models.CharField(max_length=13, default="")
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10, default="")
    vip = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=120, default="")
    city = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=50, default="")
    phone1 = models.CharField(max_length=13, default="")
    phone2 = models.CharField(max_length=13, default="")
    email = models.CharField(max_length=30, default="")
    birth_date = models.CharField(max_length=20, default="")
    reg_date = models.CharField(max_length=20, default="")
    family_ids = models.CharField(max_length=150, default="")
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


class Stock(models.Model):
    item_id = models.CharField(max_length=15)
    name = models.CharField(max_length=30, default="")
    item_picture = models.ImageField(blank=True, null=True)
    item_firm = models.CharField(max_length=20, default="")
    item_barcode = models.CharField(max_length=60, default="")
    input_cost = models.CharField(max_length=4, default="")
    output_cost = models.CharField(max_length=4, default="")
    creation_date = models.CharField(max_length=20, default="")
    exp_date = models.CharField(max_length=20, default="")
    package_num = models.CharField(max_length=20, default="")
    item_count = models.CharField(max_length=6, default="")
    in_stock = models.BooleanField(default=False)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.item_id)


class Texts(models.Model):
    text_id = models.CharField(max_length=1500)
    ru = models.CharField(max_length=1500)
    en = models.CharField(max_length=1500)
    he = models.CharField(max_length=1500)
    ar = models.CharField(max_length=1500)

    def __str__(self):
        return str(self.text_id)


class Langs(models.Model):
    user_id = models.CharField(max_length=20)
    lang = models.CharField(max_length=3, default='en')

    def __str__(self):
        return {"user_id": self.user_id, "lang": self.lang}


# Langs.objects.all())
