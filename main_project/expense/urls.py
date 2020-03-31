from django.urls import path
from . import views

app_name='expense'

urlpatterns = [
    path("create/<int:pk>/", views.ExpenseCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ExpenseUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ExpenseDeleteView.as_view(), name="delete"),
    path("create_flex/<int:pk>/", views.Expense_flexCreateView.as_view(), name="create_flex"),
    path("update_flex/<int:pk>/", views.Expense_flexUpdateView.as_view(), name="update_flex"),
    path("delete_flex/<int:pk>/", views.Expense_flexDeleteView.as_view(), name="delete_flex"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category_flex/create/", views.Category_flexCreateView.as_view(), name="category-create_flex"),
    path("sub/<int:pk>", views.Expense_flex_subTemplateView.as_view(), name="sub"),
    path("sub/<int:pk>/create", views.Expense_flex_subCreateView.as_view(), name="sub_create"),
]
