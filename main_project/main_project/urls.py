"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("3-months/", views.month_3.as_view(), name="m3"),
    path("6-months/", views.month_6.as_view(), name="m6"),
    path("9-months/", views.month_9.as_view(), name="m9"),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path('accounts/', include("django.contrib.auth.urls")),
    path("expense/", include("expense.urls"), name="expense"),
    path("income/", include("income.urls"), name="income"),
    path("transaction/", include("transaction.urls"), name="transaction")
]
urlpatterns += staticfiles_urlpatterns()
