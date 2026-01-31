
from django.urls import path
from . import views

app_name = "challenge"

urlpatterns = [
    path("", views.challengeTopView, name="challengeTop"),
    path("performance/", views.challengePerformance, name="challengePerformance"),
    path("failed/", views.challengeFailedView, name="challengeFailed"),
    path("success/", views.challengeSuccessView, name="challengeSuccess"),
    path("test/", views.testView, name="test"),
]
