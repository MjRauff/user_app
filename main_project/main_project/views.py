from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import random
import datetime
import calendar

# Models
from income.models import Income, Income_flex
from expense.models import Expense, Category, Expense_flex, Expense_flex_sub, Category_flex

def budget(user):
    expenses_flex = Expense_flex.objects.filter(user=user)
    return expenses_flex.aggregate(Sum('budget'))["budget__sum"]

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def chart_data(user, month, account):
    income = Income.objects.filter(user=user).order_by("date_payment")
    expenses = Expense.objects.filter(user=user).order_by("date_payment")
    expenses_flex = Expense_flex.objects.filter(user=user).order_by("title")
    beta = []
    alpha = []
    dt = datetime.date.today()
    date = add_months(dt, month)
    for x in income:
        beta.append((date.year, date.month, x.date_payment, x.amount, x.title))
    for x in expenses:
        beta.append((date.year, date.month, x.date_payment, -x.amount, x.title))
    budget1 = budget(user)/4
    beta.append((date.year, date.month, 7, -budget1, "Weekly budegt"))
    beta.append((date.year, date.month, 14, -budget1, "Weekly budegt"))
    beta.append((date.year, date.month, 21, -budget1, "Weekly budegt"))
    beta.append((date.year, date.month, 28, -budget1, "Weekly budegt"))
    beta.sort()
    for x in beta:
        y = x[0]
        m = x[1]
        d = x[2]
        a = x[3]
        s = x[3] + account
        t = x[4]
        account = s
        alpha.append((y, m, d, s, a, t))
    return alpha

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

    def budget(self):
        user = self.request.user
        expenses_flex = Expense_flex.objects.filter(user=user)
        return expenses_flex.aggregate(Sum('budget'))["budget__sum"]

    def budget_flex(self):
        try:
            return self.summary() - self.budget()
        except:
            return 0

    def income_summary(self):
        user = self.request.user
        income = Income.objects.filter(user=user).order_by("title")
        income_flex = Income_flex.objects.filter(user=user).order_by("title")
        income_total = income.aggregate(Sum('amount'))["amount__sum"]
        income_total_flex = income_flex.aggregate(Sum('amount'))["amount__sum"]
        if income_total == None:
            income_total = 0
        if income_total_flex == None:
            income_total_flex = 0
        return income_total + income_total_flex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        income = Income.objects.filter(user=user).order_by("title")
        income_flex = Income_flex.objects.filter(user=user).order_by("title")
        income_total = income.aggregate(Sum('amount'))["amount__sum"]
        income_total_flex = income_flex.aggregate(Sum('amount'))["amount__sum"]

        categoies = Category.objects.filter(user=user).order_by("category")
        categoies_flex = Category_flex.objects.filter(user=user).order_by("category")

        expenses = Expense.objects.filter(user=user).order_by("title")
        expenses_flex = Expense_flex.objects.filter(user=user).order_by("title")
        expenses_flex_sub = Expense_flex_sub.objects.filter(user=user).order_by("title")

        account = 1000
        m1 = chart_data(user, 0, account)
        m1_account = m1[-1:][0][3]
        m2 = chart_data(user, 1, m1_account)
        m2_account = m2[-1:][0][3]
        m3 = chart_data(user, 2, m2_account)
        m3_account = m3[-1:][0][3]
        m4 = chart_data(user, 0, m3_account)
        m4_account = m4[-1:][0][3]
        m5 = chart_data(user, 1, m4_account)
        m5_account = m5[-1:][0][3]
        m6 = chart_data(user, 2, m5_account)

        context["income"] = income
        context["income_total"] = income_total
        context["income_flex"] = income_flex
        context["income_total_flex"] = income_total_flex
        context["income_summary"] = self.income_summary()

        context["expenses"] = expenses
        context["expenses_flex"] = expenses_flex
        context["expense_total"] = expenses.aggregate(Sum('amount'))["amount__sum"]
        context["expenses_flex_sub"] = Expense_flex_sub.objects.filter(user=user).order_by("title")

        context["categoies"] = categoies
        context["categoies_flex"] = categoies_flex

        context["summary"] = self.summary()
        context["budget"] = self.budget()
        context["saving"] = self.budget_flex()

        context["chart_data"] = chart_data(user, 0, account) + chart_data(user, 1, m1_account) + chart_data(user, 2, m2_account) + chart_data(user, 3, m3_account) + chart_data(user, 4, m4_account) + chart_data(user, 5, m5_account)

        return context

class month_3(LoginRequiredMixin, generic.TemplateView):

    template_name = "forcast_chart.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        account = 1000
        m1 = chart_data(user, 0, account)
        m1_account = m1[-1:][0][3]
        m2 = chart_data(user, 1, m1_account)
        m2_account = m2[-1:][0][3]
        m3 = chart_data(user, 2, m2_account)

        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["chart_data"] = chart_data(user, 0, account) + chart_data(user, 1, m1_account) + chart_data(user, 2, m2_account)

        return context

class month_6(LoginRequiredMixin, generic.TemplateView):

    template_name = "forcast_chart.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        account = 1000
        m1 = chart_data(user, 0, account)
        m1_account = m1[-1:][0][3]
        m2 = chart_data(user, 1, m1_account)
        m2_account = m2[-1:][0][3]
        m3 = chart_data(user, 2, m2_account)
        m3_account = m3[-1:][0][3]
        m4 = chart_data(user, 0, m3_account)
        m4_account = m4[-1:][0][3]
        m5 = chart_data(user, 1, m4_account)
        m5_account = m5[-1:][0][3]
        m6 = chart_data(user, 2, m5_account)

        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["chart_data"] = chart_data(user, 0, account) + chart_data(user, 1, m1_account) + chart_data(user, 2, m2_account) + chart_data(user, 3, m3_account) + chart_data(user, 4, m4_account) + chart_data(user, 5, m5_account)

        return context

class month_9(LoginRequiredMixin, generic.TemplateView):

    template_name = "forcast_chart.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        account = 1000
        m1 = chart_data(user, 0, account)
        m1_account = m1[-1:][0][3]
        m2 = chart_data(user, 1, m1_account)
        m2_account = m2[-1:][0][3]
        m3 = chart_data(user, 2, m2_account)
        m3_account = m3[-1:][0][3]
        m4 = chart_data(user, 0, m3_account)
        m4_account = m4[-1:][0][3]
        m5 = chart_data(user, 1, m4_account)
        m5_account = m5[-1:][0][3]
        m6 = chart_data(user, 2, m5_account)
        m6_account = m6[-1:][0][3]
        m7 = chart_data(user, 0, m6_account)
        m7_account = m7[-1:][0][3]
        m8 = chart_data(user, 1, m7_account)
        m8_account = m8[-1:][0][3]
        m9 = chart_data(user, 2, m8_account)

        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["chart_data"] = chart_data(user, 0, account) + chart_data(user, 1, m1_account) + chart_data(user, 2, m2_account) + chart_data(user, 3, m3_account) + chart_data(user, 4, m4_account) + chart_data(user, 5, m5_account) + chart_data(user, 6, m6_account) + chart_data(user, 7, m7_account) + chart_data(user, 8, m8_account)

        return context
