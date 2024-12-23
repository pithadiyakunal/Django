import logging
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class EmployeeDetails(APIView):
    # List all employees
    def get(self, request):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            logger.info("Get All Employee")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error while retrieving employees: {e}")
            return Response({'error': 'Unable to fetch employees'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Create a new employee
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("New employee created successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Invalid data for creating employee: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error while creating an employee: {e}")
            return Response({'error': 'Unable to create employee'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeDetailView(APIView):
    # Retrieve a single employee
    def get(self, request, pk):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error while retrieving employee with ID {pk}: {e}")
            return Response({'error': 'Unable to fetch employee'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Update an existing employee
    def put(self, request, pk):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Employee with ID {pk} updated successfully")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.warning(f"Invalid data for updating employee with ID {pk}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error while updating employee with ID {pk}: {e}")
            return Response({'error': 'Unable to update employee'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Delete an employee
    def delete(self, request, pk):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            employee.delete()
            logger.info(f"Employee with ID {pk} deleted successfully")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error while deleting employee with ID {pk}: {e}")
            return Response({'error': 'Unable to delete employee'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class EmployeeDetails(APIView):

#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return render(request, 'employee_list.html', {'employees': serializer.data})

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('employee_list')  # Redirect to employee list page
#         return render(request, 'employee_form.html', {'errors': serializer.errors})


# class EmployeeDetailView(APIView):
#     def get(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return render(request, 'employee_form.html', {'employee': serializer.data, 'pk': pk})

#     def put(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('employee_list')
#         return render(request, 'employee_form.html', {'errors': serializer.errors, 'employee': serializer.data})

#     def delete(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         if request.method == "POST":
#             employee.delete()
#             return redirect('employee_list')
#         return render(request, 'employee_confirm_delete.html', {'employee': employee})





