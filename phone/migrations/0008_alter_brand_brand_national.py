# Generated by Django 4.2.4 on 2023-08-14 14:23

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0007_alter_phonemodel_creator_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_national',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='ملیت برند'),
        ),
    ]
