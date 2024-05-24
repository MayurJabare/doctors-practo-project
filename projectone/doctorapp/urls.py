from django.urls import path, include
from doctorapp import views

urlpatterns = [
    # path('', views.handle, name='handle data'),
    path('', views.doctor_list, name='doctor list data'),
]
