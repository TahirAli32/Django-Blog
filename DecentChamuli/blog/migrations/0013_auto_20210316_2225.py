# Generated by Django 3.1.7 on 2021-03-16 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210316_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fb_url',
            new_name='facebook_url',
        ),
    ]
