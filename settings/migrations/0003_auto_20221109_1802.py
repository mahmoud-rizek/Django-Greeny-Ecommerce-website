# Generated by Django 3.2 on 2022-11-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_rename_conct_us_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Addrees',
            field=models.TextField(max_length=100, verbose_name='Company Addrees'),
        ),
        migrations.AlterField(
            model_name='company',
            name='Cphone',
            field=models.TextField(max_length=100, verbose_name='Company Phone'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.TextField(max_length=100, verbose_name='Company email'),
        ),
    ]
