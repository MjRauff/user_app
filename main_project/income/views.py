from django.views import generic
from .models import Income
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
