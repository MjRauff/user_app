from django.views import generic
import datetime
from . import models
# Create your views here.

class TestView(generic.TemplateView):
    template_name="transaction/test.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = datetime.date.today()
        last_update = models.Updatecheck.objects.filter().first()

        context["today"] = today
        context["user"] = user
        context["last_update"] = last_update
        return context
