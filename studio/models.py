from django.db import models
class contamination(models.Model):
    date=models.DateField()
    A_COD=models.FloatField()
    A_NH4=models.FloatField()
    A_NO2=models.FloatField()
    A_NO3=models.FloatField()
    A_MLSS=models.FloatField()
    O1_COD=models.FloatField()
    O1_NH4=models.FloatField()
    O1_NO2=models.FloatField()
    O1_NO3=models.FloatField()
    O1_MLSS=models.FloatField()
    O2_COD=models.FloatField()
    O2_NH4=models.FloatField()
    O2_NO2=models.FloatField()
    O2_NO3=models.FloatField()
    O2_MLSS=models.FloatField()
    O3_COD=models.FloatField()
    O3_NH4=models.FloatField()
    O3_NO2=models.FloatField()
    O3_NO3=models.FloatField()
    O3_MLSS=models.FloatField()
    O4_COD=models.FloatField()
    O4_NH4=models.FloatField()
    O4_NO2=models.FloatField()
    O4_NO3=models.FloatField()
    O4_MLSS=models.FloatField()
    def __str__(self):
        return str(self.date)
    

# Create your models here.
