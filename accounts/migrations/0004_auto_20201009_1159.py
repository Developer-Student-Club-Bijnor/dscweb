# Generated by Django 3.1 on 2020-10-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200827_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/profile1.png', null=True, upload_to='images'),
        ),
    ]