from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser , BaseParser , MultiPartParser
from django.core.files.storage import default_storage
# from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView , DestroyAPIView ,UpdateAPIView
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
# from rest_framework.decorators import list_route
from rest_framework.decorators import action , api_view

from rest_framework.viewsets import GenericViewSet
# viewsets.ModelViewSet
class DepartmentViewSet(viewsets.ModelViewSet):
        
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
               
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department,data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    @action(detail=True, methods=['delete'])
    def delete(self, request,pk=0,format=None):
        department = Departments.objects.get(DepartmentId=pk)
        department.delete()
        
        return JsonResponse('deleted succesfully',safe=False)
    
   
    
  

class EmployeeViewSet(viewsets.ModelViewSet):
    
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
               
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee,data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update successfully",safe=False)
# class FileUploadView(views.APIView):
#        parser_classes = (FileUploadParser,)

#        def put(self, filename,request ,format=None):
#            file_obj = request.FILES['file']
#         #    file_obj.save()
#            # do some stuff with uploaded file
#            return Response(status=204)
@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)

    # -------------------------------------------------------------------------------------
# @api_view([ 'DELETE'])
# @csrf_exempt
# def departmentApi(request, pk=0,format=None):
#     if request.method == "GET":
#         departments = Departments.objects.all()
#         departments_serializer = DepartmentSerializer(departments,many = True)
#         return JsonResponse(departments_serializer.data,safe=False)
#     elif request.method == "POST":
        # department_data = JSONParser().parse(request)
#         department_serializer = DepartmentSerializer(data = department_data) 
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("added successfully",safe=False)
#         return JsonResponse("Failed to add",safe=False)
#     elif request.method == "PUT":
#         department_data = JSONParser().parse(request)
#         department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
#         department_serializer = DepartmentSerializer(department,data = department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Update successfully",safe=False)
#         return JsonResponse("Failed to update",safe=False)
#     elif request.method == "DELETE":
        # department = Departments.objects.get(DepartmentId=pk)
        # department.delete()
        # return JsonResponse('deleted succesfully',safe=False)


