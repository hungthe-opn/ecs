from django.urls import path
from .views import RepositoryPostType, RepositoryView, AddProductView


app_name = 'repository'

urlpatterns = [
    path('', RepositoryView.as_view(), name='repository_list'),
    path('repo/<pk>', RepositoryPostType.as_view(), name='repository_name'),
    path('import/<pk>', AddProductView.as_view(), name='repository_import'),

]