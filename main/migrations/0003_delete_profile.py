# Generated by Django 4.2 on 2023-05-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_danpolz_options_alter_danpolz_nickname_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]