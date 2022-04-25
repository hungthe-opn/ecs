from django.urls import path
from .views import ListAssetView


app_name = 'manage_asset'

urlpatterns = [
    path('', ListAssetView.as_view(), name='list_manage'),

]