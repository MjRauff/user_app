from django.views import generic
from .models import Income, Income_flex
from django.urls import reverse
# Create your views here.
class IncomeCreateView(generic.CreateView):
    model = Income
    template_name = "income/create_income.html"
    fields = ("title", "amount", "date_payment")
    def form_valid(self, form):
        Income = form.save(commit=False)
        user = self.request.user
        Income.user = user
        return super(IncomeCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")

class IncomeUpdateView(generic.UpdateView):
    model = Income
    fields = ("title", "amount", "date_payment")
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["income"] = Income.objects.get(pk=self.kwargs["pk"])
        return context

class IncomeDeleteView(generic.DeleteView):
    model = Income
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["income"] = Income.objects.get(pk=self.kwargs["pk"])
        return context


class Income_flexCreateView(generic.CreateView):
    model = Income_flex
    template_name = "income/create_income_flex.html"
    fields = ("title", "amount", "date_payment")
    def form_valid(self, form):
        Income = form.save(commit=False)
        user = self.request.user
        Income.user = user
        return super(Income_flexCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")

class Income_flexUpdateView(generic.UpdateView):
    model = Income_flex
    fields = ("title", "amount", "date_payment")
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["income_flex"] = Income_flex.objects.get(pk=self.kwargs["pk"])
        return context

class Income_flexDeleteView(generic.DeleteView):
    model = Income_flex
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["income_flex"] = Income_flex.objects.get(pk=self.kwargs["pk"])
        return context
