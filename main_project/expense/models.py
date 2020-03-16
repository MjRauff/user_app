from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_payment = models.DateField()
    def __str__(self):
            return "User / {} - {}".format(self.user, self.title)
