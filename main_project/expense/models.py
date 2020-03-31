from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.db.models import Sum
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    def __str__(self):
            return "{}".format(self.category)

    def count(self):
        expenses = Expense.objects.filter(user=self.user, category=self)
        return expenses.count()

    def amount_total(self):
        expenses = Expense.objects.filter(user=self.user, category=self)
        total = expenses.aggregate(Sum('amount'))["amount__sum"]
        if total == None:
            return 0
        else:
            return total

class Category_flex(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    def __str__(self):
            return "{}".format(self.category)

    def budget_total(self):
        expenses = Expense_flex.objects.filter(user=self.user, category=self)
        total = expenses.aggregate(Sum('budget'))["budget__sum"]
        if total == None:
            return 0
        else:
            return total

    def amount_total(self):
        expenses = Expense_flex.objects.filter(user=self.user, category=self)
        expense_flex_sub = Expense_flex_sub.objects.filter(user=self.user)
        list1 = []
        for sub in expense_flex_sub:
            if sub.expense_flex in expenses:
                list1.append(sub.amount)
        return sum(list1)

    def count(self):
        expenses = Expense_flex.objects.filter(user=self.user, category=self)
        return expenses.count()

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_payment = models.IntegerField()
    def __str__(self):
            return "{} - {}".format(self.user, self.title)

class Expense_flex(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category_flex, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    budget = models.IntegerField()
    def sub_count(self):
        sub = Expense_flex_sub.objects.filter(user=self.user, expense_flex=self)
        return sub.count()
    def amount_total(self):
        sub = Expense_flex_sub.objects.filter(user=self.user, expense_flex=self)
        sub_amount = sub.aggregate(Sum('amount'))["amount__sum"]
        if sub_amount == None:
            return 0
        else:
            return sub_amount
    def __str__(self):
            return "{} - {}".format(self.user, self.title)

class Expense_flex_sub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    expense_flex = models.ForeignKey(Expense_flex, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    def __str__(self):
            return "{} - {}".format(self.user, self.title)

def create_profile(sender, **kwargs):
    if kwargs["created"]:
        category = Category.objects.create(user=kwargs["instance"], category="Housing")
        category = Category.objects.create(user=kwargs["instance"], category="Bills")
        category = Category.objects.create(user=kwargs["instance"], category="Debt")
        category = Category.objects.create(user=kwargs["instance"], category="Subscriptions")

def create_profile(sender, **kwargs):
    if kwargs["created"]:
        category = Category.objects.create(user=kwargs["instance"], category="Housing")
        category = Category.objects.create(user=kwargs["instance"], category="Bills")
        category = Category.objects.create(user=kwargs["instance"], category="Debt")
        category = Category.objects.create(user=kwargs["instance"], category="Subscriptions")


post_save.connect(create_profile, sender=User)
