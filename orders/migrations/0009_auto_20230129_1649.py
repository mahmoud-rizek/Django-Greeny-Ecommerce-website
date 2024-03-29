# Generated by Django 3.2 on 2023-01-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20230124_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(null=0),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
