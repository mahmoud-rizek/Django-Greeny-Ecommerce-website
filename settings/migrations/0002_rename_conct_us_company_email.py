# Generated by Django 3.2 on 2022-11-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='conct_us',
            new_name='email',
        ),
    ]
