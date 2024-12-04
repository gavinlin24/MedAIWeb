from django.db import models

class PatientDemographics(models.Model):
    patient_id = models.CharField(max_length=20, primary_key=True)
    gender = models.CharField(max_length=10)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"

class TestDemographics(models.Model):
    patient = models.ForeignKey(PatientDemographics, on_delete=models.CASCADE)
    acquisition_date = models.DateField()

    def __str__(self):
        return f"Test {self.id} for Patient {self.patient.patient_id} on {self.acquisition_date}"

class RestingECG(models.Model):
    patient = models.ForeignKey(PatientDemographics, on_delete=models.CASCADE)
    ventricular_rate = models.IntegerField()
    atrial_rate = models.IntegerField()
    qrs_duration = models.IntegerField()
    qt_interval = models.IntegerField()
    qt_corrected = models.IntegerField()
    r_axis = models.IntegerField()
    t_axis = models.IntegerField()

    def __str__(self):
        return f"Resting ECG for Patient {self.patient.patient_id} Test {self.id}"

