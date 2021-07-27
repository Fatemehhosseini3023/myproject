from EmployeeApp.views import  *
from rest_framework import renderers
from django.urls import path , re_path ,include
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# router = DefaultRouter()
# router.register(r'departments', DepartmentViewSet)
department_list = DepartmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
department_detail = DepartmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = format_suffix_patterns([
   
    path('departments/', department_list, name='department_list'),
    path('departments/<int:pk>/', department_detail, name='department_detail'),
    # path('departments/delete/<int:pk>/', departmentApi, name='department_delete'),
    path('employees/', employee_list, name='employee_list'),
    path('employeets/<int:pk>/', employee_detail, name='employee_detail'),
    path('upload/',SaveFile),
     
    
    # re_path(r'^upload/', SaveFile)
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail')
])
# urlpatterns = [
#     path('', include(router.urls)),
# ]
