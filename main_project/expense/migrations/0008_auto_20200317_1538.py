# Generated by Django 3.0.3 on 2020-03-17 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_auto_20200317_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='categories',
            new_name='category',
        ),
    ]
