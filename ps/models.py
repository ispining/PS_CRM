from django.db import models

# Create your models here.
from django.db import models



class Worker(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teudat_zeut = models.CharField(max_length=10)
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10)
    vip = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=10)
    reg_date = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    special_files = models.FileField(blank=True, null=True)

class Agent(models.Model):
    affiliate_id = models.CharField(max_length=10)
    affiliate_name = models.CharField(max_length=20)
    parent_company = models.CharField(max_length=20)
    staff_ids = models.CharField(max_length=100)
    affiliate_country = models.CharField(max_length=20)
    affiliate_city = models.CharField(max_length=20)
    affiliate_location = models.CharField(max_length=50)
    affiliate_percent = models.CharField(max_length=2)
    phone1 = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=15)
    contact_id = models.CharField(max_length=10)
    reg_date = models.CharField(max_length=20)
    special_files = models.FileField(blank=True, null=True)


class Lead(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    teudat_zeut = models.CharField(max_length=13)
    profile_picture = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10)
    vip = models.CharField(max_length=10)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50, default="")
    phone1 = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=20)
    reg_date = models.CharField(max_length=20)
    family_ids = models.CharField(max_length=150)
    special_files = models.FileField(blank=True, null=True)


class Stock(models.Model):
    row_id = models.CharField(max_length=10)
    item_id = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    item_picture = models.ImageField(blank=True, null=True)
    item_firm = models.CharField(max_length=20)
    item_barcode = models.CharField(max_length=60)
    input_cost = models.CharField(max_length=4)
    output_cost = models.CharField(max_length=4)
    creation_date = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=20)
    package_num = models.CharField(max_length=20)
    item_count = models.CharField(max_length=6)
    in_stock = models.BooleanField(default=False)
    special_files = models.FileField(blank=True, null=True)


class Texts(models.Model):
    text_id = models.CharField(max_length=1500)
    ru = models.CharField(max_length=1500)
    en = models.CharField(max_length=1500)
    he = models.CharField(max_length=1500)
    ar = models.CharField(max_length=1500)


class langs(models.Model):
    user_id = models.CharField(max_length=20)
    lang = models.CharField(max_length=3)