# Generated by Django 3.1.2 on 2020-11-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20201129_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(null=True, upload_to='')),
                ('Schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.schedule')),
            ],
        ),
    ]
