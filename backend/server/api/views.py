from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientDemographics
from .serializers import PatientDemographicsSerializer
from .renderers import CustomXMLRenderer

class PatientXMLView(ListAPIView):
    serializer_class = PatientDemographicsSerializer
    renderer_classes = [CustomXMLRenderer]

    def get_queryset(self):
        query_set = PatientDemographics.objects.all()
        patient_id = self.request.query_params.get('patient_id')

        if patient_id:
            query_set = query_set.filter(patient_id=patient_id)
        
        return query_set
    
    '''
    GET method for patient(s)

    / : returns all patients in database 
    /?patient_id= : returns patient with patient id
    '''
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response(
                {"error": "No patient found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)