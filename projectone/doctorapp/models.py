from django.db import models


class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    clinic_name = models.CharField(max_length=255, blank=True, null=True)
    consultation_fee = models.CharField(max_length=255, blank=True, null=True)
    recommendation = models.CharField(max_length=255, blank=True, null=True)
    patient_stories = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_info'

    def __str__(self) -> str:
        return f'{self.doctor_name}'
