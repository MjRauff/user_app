from django.urls import path
from . import views

app_name='expense'

urlpatterns = [
    path("create/<int:pk>/", views.ExpenseCreateView.as_view(), name="create"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("test/", views.TemplateView.as_view(), name="test")
]
