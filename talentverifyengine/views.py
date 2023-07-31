from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee, Students
from .serializer import CompanySerializer, EmployeeSerializer, StudentsSerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser

from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render

# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class CSVUploadViews(APIView):
    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_csv(csv_file)

            for row in df.iterrows():
                data = row[1]
                # Process the row data and save it to the database
                # Replace 'YourModel' with your actual model name

                try:
                    Students.objects.create(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    marks = data['marks'],
                    roll_number = data['roll_number'],
                    section = data['section']
                        # Add more fields as per your CSV file
                    )
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_201_CREATED)
        except pd.errors.ParserError as e:
            return Response({'error': 'Unable to parse CSV file'}, status=status.HTTP_400_BAD_REQUEST)



class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                Students.objects.create(
                    first_name = record['first_name'],
                    last_name = record['last_name'],
                    marks = record['marks'],
                    roll_number = record['roll_number'],
                    section = record['section']
                )
            except Exception as e:
                context['exceptions_raised'] = e
                
        return render(request, self.template_name, context)

class CSVUploadView(APIView):
    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_csv(csv_file)

            for row in df.iterrows():
                record = row[1]
                
                # Process the row data and save it to the database
                # Replace 'YourModel' with your actual model name

                try:
                    # print('jhdjs')
                    Company.objects.create(
                    name= record['name'],
                    date_of_registration= record['date_of_registration'],
                    company_registration_number= record['company_registration_number'],
                    address= record['address'],
                    contact_person= record['contact_person'],
                    departments= record['departments'],
                    num_employees= record['num_employees'],
                    # employees= record['employees'],
                    contact_phone= record['contact_phone'],
                    email= record['email'],
                        # Add more fields as per your CSV file
                    )
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_201_CREATED)
        except pd.errors.ParserError as e:
            return Response({'error': 'Unable to parse CSV file'}, status=status.HTTP_400_BAD_REQUEST)
        
#view for uploading employess via csv        
class EmployeeCsvUploadView(APIView):
    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_csv(csv_file)

            for row in df.iterrows():
                record = row[1]
                
                # Process the row data and save it to the database
                # Replace 'YourModel' with your actual model name

                try:
                    # print('jhdjs')
                    Employee.objects.create(
                    name= record['name'],
                    employee_id_number = record['employee_id_number'],
                    department = record['department'],
                    role = record['role'],
                    date_started = record['date_started'],
                    duties = record['duties'],
                    )
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_201_CREATED)
        except pd.errors.ParserError as e:
            return Response({'error': 'Unable to parse CSV file'}, status=status.HTTP_400_BAD_REQUEST)


                    

# class CSVUploadView(APIView):
#     parser_classes = (FormParser, MultiPartParser)
#     def post(self, request):
#         for file in request.FILES.values():

#             decoded_file = csv_file.read().decode('utf-8')
#             csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
#             # reader = csv.reader(file) 
#             objects = []
#             for row in reader:
#                 objects.append(Company( 
#                     # city=row[0], 
#                     # wheel_type=row[1], # and so on .. 
#                     name= row[0],
#                     date_of_registration= row[1],
#                     company_registration_number= row[2],
#                     address= row[3],
#                     contact_perso= row[4],
#                     departments= row[5],
#                     num_employees= row[6],
#                     employees= row[7],
#                     contact_phone= row[8],
#                     email= row[9],
#                 )) 
#             Company.objects.bulk_create(objects) 
#         return Response({"success": "Good job, buddy"})

    # def post(self, request):
    #     csv_file = request.FILES['csv_file']
    #     decoded_file = csv_file.read().decode('utf-8')
    #     csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        
    #     # Process the CSV data and append it to the database
    #     # Replace 'MyModel' with your actual model name
        
    #     for row in csv_data:
    #         print(row)
    #         new_data = {
    #             # 'field1': row[0],
    #             # 'field2': row[1],
                
                # 'name': row[0],
                # 'date_of_registration': row[1],
                # 'company_registration_number': row[2],
                # 'address': row[3],
                # 'contact_person': row[4],
                # 'departments': row[5],
                # 'num_employees': row[6],
                # 'employees': row[7],
                # 'contact_phone': row[8],
                # 'email': row[9],
    #             # Add more fields as per your CSV file
    #         }
            
    #         Company.objects.create(**new_data)
        
    #     return Response(status=status.HTTP_201_CREATED)



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class CompanyListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class EmployeeListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class CompanyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer