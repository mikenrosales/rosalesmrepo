from django.urls import path
from . import views

app_name = 'myportfolio'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='myportfolio'),
]

