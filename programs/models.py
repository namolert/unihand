from django.db import models

class Program(models.Model):
    program_code = models.CharField(max_length=20, unique=True)
    program_name = models.CharField(max_length=255)

    def __str__(self):
        return self.program_name
