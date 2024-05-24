from django.urls import path, include
from doctorapp import views



urlpatterns = [
    path('', views.doctor_list, name='doctor list data'),
    path('refresh_table', views.update_doctor_table, name='update doctor table data'),
]

