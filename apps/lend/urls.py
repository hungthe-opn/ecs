from django.urls import path
from .views import LendView, SearchLendView, ListLentView, EndRemoteView, CreateRemoteView, UploadRemoteView, \
    ListDepartmentsView, AssetDepartmentsView, DeviceLendView, AssetDepartmentsExportView, \
    InsuranceView, EndInventoryView, DeviceLendExportView, NotifyView, ImportLendRepository, ExportLendRepository, \
    AddRemotedView, AddInsuranceView

app_name = 'lend'

urlpatterns = [
    path('', LendView.as_view(), name='lend_listview'),
    path('list/', ListLentView.as_view(), name='lend_list_employee_id'),
    path('search/<pk>', SearchLendView.as_view(), name='lend_remote'),
    path('endremote/<pk>', EndRemoteView.as_view(), name='end_remote'),
    path('created/', CreateRemoteView.as_view(), name='lend_created'),
    path('upload/<pk>', UploadRemoteView.as_view(), name='lend_upload'),
    path('assert/', AssetDepartmentsView.as_view(), name='lend_assert'),
    path('assertexport/<pk>', AssetDepartmentsExportView.as_view(), name='lend_assert_export'),
    path('departments/', ListDepartmentsView.as_view(), name='list_departments'),
    path('device/', DeviceLendView.as_view(), name='list_device'),
    path('createdevice/', DeviceLendExportView.as_view(), name='create_device'),
    path('insurance/', InsuranceView.as_view(), name='insurance'),
    path('endinsurance/<pk>', EndInventoryView.as_view(), name='end_insurance'),
    path('addinsurance/<pk>', AddInsuranceView.as_view(), name='add_insurance'),
    path('notify/', NotifyView.as_view(), name='notify_message'),
    path('importlend/<pk>', ImportLendRepository.as_view(), name='import_lend'),
    path('exportlend/<pk>', ExportLendRepository.as_view(), name='export_lend'),
    path('addremote/', AddRemotedView.as_view(), name='add_remote'),
]