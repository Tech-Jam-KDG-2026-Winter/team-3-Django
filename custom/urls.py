from django.urls import path
from . import views

app_name="custom"

urlpatterns = [
    path('', views.custom_home_view,name="custom_home"),
]