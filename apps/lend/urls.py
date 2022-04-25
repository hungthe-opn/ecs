from django.urls import path
from .views import LendView, SearchLendView, ListLentView, EndRemoteView,  CreateRemoteView,UploadRemoteView, ListDepartmentsView, AssetDepartmentsView, DeviceLendView,DeviceLendSerializer


app_name = 'lend'

urlpatterns = [
    path('', LendView.as_view(), name='lend_listus'),
    path('list/', ListLentView.as_view(), name='lend_list'),
    path('search/<pk>', SearchLendView.as_view(), name='lend_remote'),
    path('change/<pk>', EndRemoteView.as_view(), name='change'),
    path('created', CreateRemoteView.as_view(), name='lend_created'),
    path('upload/<pk>', UploadRemoteView.as_view(), name='lend_upload'),
    path('assert/', AssetDepartmentsView.as_view(), name='lend_assert'),
    path('departments/', ListDepartmentsView.as_view(), name='list_departments'),
    path('device/', DeviceLendView.as_view(), name='list_device'),
    path('createdevice/', DeviceLendSerializer.as_view(), name='create_device'),
]