from django.urls import path
from geekapp import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('host/',views.host, name='host'),
    path('end/',views.end, name="end"),
    path('welcome/<name>/<pk>',views.submittedform, name='submittedform')
]
