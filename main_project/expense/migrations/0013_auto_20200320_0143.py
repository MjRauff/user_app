# Generated by Django 3.0.3 on 2020-03-20 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0012_expense_flex_sub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense_flex_sub',
            old_name='budget',
            new_name='amount',
        ),
    ]
