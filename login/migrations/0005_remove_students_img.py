# Generated by Django 3.1.2 on 2020-11-28 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_students_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='img',
        ),
    ]
