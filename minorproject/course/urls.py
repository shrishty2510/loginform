from django.urls import path
from course import views

urlpatterns = [
    path('',views.index),
    path('learndj/',views.learn_django),
    path('learnmt/',views.learn_math),
    path('learnvr/',views.learn_var),
    path('learnft/',views.learn_format),
    path('learnpy/',views.learn_python),
    
]
