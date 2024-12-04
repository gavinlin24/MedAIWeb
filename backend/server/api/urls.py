from django.urls import path
from .views import PatientXMLView

urlpatterns = [
    path('', PatientXMLView.as_view(), name='patient-xml'),
]