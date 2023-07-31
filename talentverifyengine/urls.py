from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CSVUploadView, CsvUploader, CSVUploadViews, RegisterAPI, EmployeeCsvUploadView

from knox import views as knox_views
from .views import LoginAPI
from django.urls import path


from django.urls import re_path as url

router = routers.DefaultRouter()

router.register('companies', views.CompanyViewSet)
router.register('employees', views.EmployeeViewSet)
# router.register('register', views.RegisterAPI)
# router.register('students', views.StudentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/upload-csv/', CSVUploadView.as_view(), name='csv-upload'),
    path('api/employee_upload_csv/', EmployeeCsvUploadView.as_view(), name='employee_csv_upload'),
    # path('api/upload-csv/', CsvUploader.as_view(), name='csv-upload'),
    path('api/', include(router.urls), name='api'),
    url('^csv-uploader/$', CsvUploader.as_view(), name='csv-uploader'),
    path('api/upload-csvs/', CSVUploadViews.as_view(), name='csv-upload'),
     path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]