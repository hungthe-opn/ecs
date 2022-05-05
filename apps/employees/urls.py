from django.urls import path
from .views import EmployeesView

app_name = 'employees'

urlpatterns = [
    path('', EmployeesView.as_view(), name='employee'),
    # path('list/', ListLentView.as_view(), name='lend_list'),
    # path('search/<pk>', SearchLendView.as_view(), name='lend_remote'),
]