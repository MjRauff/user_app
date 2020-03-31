from django.db import models
import datetime
from expense.models import Expense
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Updatecheck(models.Model):
    last_update = models.DateField()

    def months_past(self):
        today = datetime.date.today()
        date = self.last_update
        year = (today.year - date.year) * 12
        month = today.month - date.month
        return month + year


    def check_for_update(self):
        today = datetime.date.today()
        if today <= self.last_update:
            return "No need for an update / {}".format(today)
        elif today > self.last_update:
            months_past = self.months_past()
            return months_past
        else:
            print("ERROR")

    def __str_(self):
        return self.pk

class Transaction(models.Model):
    pass

# def test(sender, **kwargs):
#     if kwargs["created"]:
#         print(kwargs)
#         print(request.user)
#
# post_save.connect(test, sender=Expense)
