

from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=100)
    redirect_path = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Field(models.Model):
    form = models.ForeignKey(Form, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    required = models.BooleanField(default=False)
    readable = models.BooleanField(default=False)
    

    def _str_(self):
        return f"{self.form.name} - {self.name}"
