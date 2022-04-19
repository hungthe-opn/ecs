from django.urls import path
from .views import TypeView


app_name = 'type'

urlpatterns = [
    path('', TypeView.as_view(), name='type_list'),
]