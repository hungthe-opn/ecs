from django.urls import path
from .views import RepositoryPostType


app_name = 'repository'

urlpatterns = [
    path('', RepositoryPostType.as_view(), name='repository_name'),
]