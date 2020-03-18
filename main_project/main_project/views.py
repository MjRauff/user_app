from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from income.models import Income
from expense.models import Expense, Category

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy('accounts:login')

    def summary(self):
        user = self.request.user
        income = Income.objects.filter(user=user)
        expense = Expense.objects.filter(user=user)
        try:
            e = expense.aggregate(Sum('amount'))["amount__sum"]
            if e == None:
                e = 0
            i = income.aggregate(Sum('amount'))["amount__sum"]
            if i == None:
                i = 0
        except:
            pass
        return i - e

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        income = Income.objects.filter(user=user).order_by("title")
        categoies = Category.objects.filter(user=user).order_by("category")
        expenses = Expense.objects.filter(user=user).order_by("title")
        context["income"] = income
        context["income_total"] = income.aggregate(Sum('amount'))["amount__sum"]
        context["expenses"] = expenses
        context["expense_total"] = expenses.aggregate(Sum('amount'))["amount__sum"]
        context["categoies"] = categoies
        context["summary"] = self.summary()

        return context
