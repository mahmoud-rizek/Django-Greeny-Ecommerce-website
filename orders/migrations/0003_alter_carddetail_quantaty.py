# Generated by Django 3.2 on 2022-11-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20221102_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetail',
            name='quantaty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
