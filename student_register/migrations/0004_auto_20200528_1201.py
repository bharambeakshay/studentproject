# Generated by Django 2.2 on 2020-05-28 06:31

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0003_auto_20200528_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]