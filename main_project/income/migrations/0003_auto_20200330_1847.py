# Generated by Django 3.0.3 on 2020-03-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_income_flex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date_payment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='income_flex',
            name='date_payment',
            field=models.IntegerField(),
        ),
    ]
