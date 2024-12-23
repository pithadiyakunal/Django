from django.urls import path
from .views import EmployeeDetails, EmployeeDetailView
# import views
# from myapp.views import home


urlpatterns = [
    path('employees/', EmployeeDetails.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    # path('api/employees/', EmployeeDetails.as_view(), name='employee_list'),
    # path('api/employees/new/', EmployeeDetails.as_view(), name='employee_create'),
    # path('api/employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_update'),
    # path('api/employees/<int:pk>/delete/', EmployeeDetailView.as_view(), name='employee_delete'),
]

