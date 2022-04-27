from django.urls import path
from .views import ImportManageView, ExportManageView

app_name = 'manage_asset'

urlpatterns = [
    path('import/', ImportManageView.as_view(), name='import'),
    path('export/', ExportManageView.as_view(), name='export'),
]