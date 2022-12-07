# Generated by Django 3.2 on 2022-11-09 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20221109_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(default=django.utils.timezone.now)),
                ('value', models.FloatField()),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
    ]