from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Tm(models.Model):
    staff_name = models.CharField(max_length=100)
    tm_date = models.DateField()
    application = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    duration = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(24.0)])
    public_id = models.IntegerField()
    public_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.staff_name