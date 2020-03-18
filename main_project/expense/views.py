from django.views import generic
from django.urls import reverse
from .models import Category, Expense
from django.contrib.auth.mixins import LoginRequiredMixin

class ExpenseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Expense
    template_name = "expense/create_expense.html"
    fields = ("title", "amount", "date_payment")
    def form_valid(self, form):
        Expense = form.save(commit=False)
        user = self.request.user
        Expense.user = user
        Expense.category = Category.objects.get(pk=self.kwargs['pk'])
        return super(ExpenseCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")

class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = "expense/create_category.html"
    fields = ('category',)
    def form_valid(self, form):
        Category = form.save(commit=False)
        Category.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")

class TemplateView(generic.TemplateView):
    template_name = "expense/test.html"
