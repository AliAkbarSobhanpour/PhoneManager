# Generated by Django 4.2.4 on 2023-08-10 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_remove_phonemodel_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='phone_size',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0, 'مقدار مورد نظر باید بیشتر از 0 باشد.')], verbose_name='سایز گوشی همراه'),
        ),
    ]