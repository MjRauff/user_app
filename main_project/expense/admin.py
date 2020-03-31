from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Expense)
admin.site.register(models.Category)
admin.site.register(models.Expense_flex)
admin.site.register(models.Expense_flex_sub)
admin.site.register(models.Category_flex)
