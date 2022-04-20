from django.urls import path
from .views import LendView, SearchLendView, ListLentView

app_name = 'lend'

urlpatterns = [
    path('', LendView.as_view(), name='lend_listus'),
    path('list/', ListLentView.as_view(), name='lend_list'),
    path('search/<pk>', SearchLendView.as_view(), name='lend_remote'),
]