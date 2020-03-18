from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.db.models import Sum

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    def __str__(self):
            return "{}".format(self.category)

    def amount_total(self):
        expenses = Expense.objects.filter(user=self.user, category=self)
        total = expenses.aggregate(Sum('amount'))["amount__sum"]
        if total == None:
            return 0
        else:
            return total


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_payment = models.DateField()
    def __str__(self):
            return "User / {} - {}".format(self.user, self.title)

def create_profile(sender, **kwargs):
    if kwargs["created"]:
        category = Category.objects.create(user=kwargs["instance"], category="Housing")
        category = Category.objects.create(user=kwargs["instance"], category="Bills")
        category = Category.objects.create(user=kwargs["instance"], category="Debt")
        category = Category.objects.create(user=kwargs["instance"], category="Subscriptions")


post_save.connect(create_profile, sender=User)
