# Generated by Django 4.1.4 on 2022-12-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliate_id', models.CharField(max_length=10)),
                ('affiliate_name', models.CharField(max_length=20)),
                ('parent_company', models.CharField(max_length=20)),
                ('staff_ids', models.CharField(max_length=100)),
                ('affiliate_country', models.CharField(max_length=20)),
                ('affiliate_city', models.CharField(max_length=20)),
                ('affiliate_location', models.CharField(max_length=50)),
                ('affiliate_percent', models.CharField(max_length=2)),
                ('phone1', models.CharField(max_length=13)),
                ('phone2', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=30)),
                ('site', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('contact_id', models.CharField(max_length=10)),
                ('reg_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='langs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('lang', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('teudat_zeut', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=10)),
                ('vip', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('phone1', models.CharField(max_length=13)),
                ('phone2', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=30)),
                ('birth_date', models.CharField(max_length=20)),
                ('reg_date', models.CharField(max_length=20)),
                ('family_ids', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.CharField(max_length=10)),
                ('item_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('item_firm', models.CharField(max_length=20)),
                ('item_barcode', models.CharField(max_length=60)),
                ('input_cost', models.CharField(max_length=4)),
                ('output_cost', models.CharField(max_length=4)),
                ('creation_date', models.CharField(max_length=20)),
                ('exp_date', models.CharField(max_length=20)),
                ('package_num', models.CharField(max_length=20)),
                ('item_count', models.CharField(max_length=6)),
                ('in_stock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_id', models.CharField(max_length=1500)),
                ('ru', models.CharField(max_length=1500)),
                ('en', models.CharField(max_length=1500)),
                ('he', models.CharField(max_length=1500)),
                ('ar', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('teudat_zeut', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('vip', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=10)),
                ('phone2', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('birth_date', models.CharField(max_length=10)),
                ('reg_date', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
