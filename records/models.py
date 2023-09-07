from django.db import models

# Create your models here.
class Log(models.Model):
    # [project_name]->[hours-minutes-seconds]:[day-month-year]
    project_name=models.CharField(max_length=50)
    time=models.DateTimeField()

    def delete(self, *args, **kwargs):
        raise Exception("Deletion of MyModel objects is not allowed.")
        
    def __str__(self):
        return f"{self.project_name} - {self.time}"