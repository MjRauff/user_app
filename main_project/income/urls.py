from django.urls import path
from . import views

app_name='income'

urlpatterns = [
    path("create/", views.IncomeCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.IncomeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.IncomeDeleteView.as_view(), name="delete"),
    path("create/flex/", views.Income_flexCreateView.as_view(), name="create_flex"),
    path("update/flex/<int:pk>/", views.Income_flexUpdateView.as_view(), name="update_flex"),
    path("delete/flex/<int:pk>/", views.Income_flexDeleteView.as_view(), name="delete_flex"),
]
