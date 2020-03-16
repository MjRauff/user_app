from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from income.models import Income
from expense.models import Expense

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

    def category(self):
        user = self.request.user
        expense_category = Expense.objects.values("category").distinct()
        l = []
        for exp in expense_category:
            e = exp["category"]
            y = Expense.objects.filter(user=user, category=e)
            y = y.aggregate(Sum('amount'))["amount__sum"]
            x = (exp["category"], y)
            l.append(x)
        return l

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        income = Income.objects.filter(user=user)
        expense = Expense.objects.filter(user=user)
        expense_housing = Expense.objects.filter(user=user, category="Housing")
        expense_bills = Expense.objects.filter(user=user, category="Bills")
        expense_debt = Expense.objects.filter(user=user, category="Debt")
        expense_Subscriptions = Expense.objects.filter(user=user, category="Subscriptions")

        context["income"] = income
        context["income_total"] = income.aggregate(Sum('amount'))["amount__sum"]
        context["expense"] = expense
        context["expense_housing"] = expense_housing
        context["expense_housing_total"] = expense_housing.aggregate(Sum('amount'))["amount__sum"]
        context["expense_bills"] = expense_bills
        context["expense_bills_total"] = expense_bills.aggregate(Sum('amount'))["amount__sum"]
        context["expense_debt"] = expense_debt
        context["expense_debt_total"] = expense_debt.aggregate(Sum('amount'))["amount__sum"]
        context["expense_subscriptions"] = expense_Subscriptions
        context["expense_subscriptions_total"] = expense_Subscriptions.aggregate(Sum('amount'))["amount__sum"]
        context["expences"] = expense.aggregate(Sum('amount'))["amount__sum"]
        context["summary"] = self.summary()
        context["category"] = self.category()

        return context
