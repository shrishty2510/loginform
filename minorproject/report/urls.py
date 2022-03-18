from django.urls import path
from report import views as r
from report.views import learn_m
urlpatterns = [
    path('learn/',r.learn_dj),
    path('learnm/',learn_m),
]
