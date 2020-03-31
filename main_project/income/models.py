from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    amount = models.IntegerField(null=True, default=0)
    date_payment = models.IntegerField()
    def __str__(self):
            return "{} - {}".format(self.user, self.title)

class Income_flex(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    amount = models.IntegerField(null=True, default=0)
    date_payment = models.IntegerField()
    def __str__(self):
            return "{} - {}".format(self.user, self.title)
