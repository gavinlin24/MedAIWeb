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
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if patient_id:
            query_set = query_set.filter(patient_id=patient_id)

        if first_name:
            query_set = query_set.filter(first_name__iexact=first_name)
        
        if last_name:
            query_set = query_set.filter(last_name__iexact=last_name)
        
        if start_date and end_date:
            query_set = query_set.filter(
                testdemographics__acquisition_date__range=[start_date, end_date]
            ).distinct()
        
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
        
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        serializer_context = {"start_date": start_date, "end_date": end_date}
        serializer = self.get_serializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)