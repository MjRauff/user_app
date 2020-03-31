from django.views import generic
from django.urls import reverse
from .models import Category, Expense, Category_flex, Expense_flex, Expense_flex_sub
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["category"] = Category.objects.get(pk=self.kwargs["pk"])
        return context

class ExpenseDeleteView(generic.DeleteView):
    model = Expense
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["expense"] = Expense.objects.get(pk=self.kwargs["pk"])
        return context

class ExpenseUpdateView(generic.UpdateView):
    model = Expense
    fields = ("title", "amount", "date_payment")
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["expense"] = Expense.objects.get(pk=self.kwargs["pk"])
        return context

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

class Expense_flexCreateView(LoginRequiredMixin, generic.CreateView):
    model = Expense_flex
    template_name = "expense/create_expense_flex.html"
    fields = ("title", "budget",)
    def form_valid(self, form):
        Expense = form.save(commit=False)
        user = self.request.user
        Expense.user = user
        Expense.category = Category_flex.objects.get(pk=self.kwargs['pk'])
        return super(Expense_flexCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["category_flex"] = Category_flex.objects.get(pk=self.kwargs["pk"])
        return context

class Expense_flexDeleteView(generic.DeleteView):
    model = Expense_flex
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["expense_flex"] = Expense_flex.objects.get(pk=self.kwargs["pk"])
        return context

class Expense_flexUpdateView(generic.UpdateView):
    model = Expense_flex
    fields = ("title", "budget",)
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["expense_flex"] = Expense_flex.objects.get(pk=self.kwargs["pk"])
        return context

class Category_flexCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category_flex
    template_name = "expense/create_category_flex.html"
    fields = ('category',)
    def form_valid(self, form):
        Category = form.save(commit=False)
        Category.user = self.request.user
        return super(Category_flexCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")

class Expense_flex_subTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "expense/expense_flex_sub_list.html"

    def get_sub_list(self):
        user = self.request.user
        pk = Expense_flex.objects.get(pk=self.kwargs["pk"])
        list = Expense_flex_sub.objects.filter(user=user, expense_flex=pk).order_by("date_created")
        return list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["list"] = self.get_sub_list()
        context["expense"] = Expense_flex.objects.get(pk=self.kwargs["pk"])
        return context

class Expense_flex_subCreateView(LoginRequiredMixin, generic.CreateView):
    model = Expense_flex_sub
    fields = ('title','amount',)
    def form_valid(self, form):
        Category = form.save(commit=False)
        Category.user = self.request.user
        return super(Expense_flex_subCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse("home")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["expense"] = Expense_flex.objects.get(pk=self.kwargs["pk"])
        return context
