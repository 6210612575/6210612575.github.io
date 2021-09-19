from django.db import models
from django.contrib.auth.models import User




class Subject(models.Model):

    class ans(models.TextChoices):
        free = "free"
        full = "full"

    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    semester = models.IntegerField(default=None, null=True)
    year = models.IntegerField(default=None, null=True)
    limited_seat = models.IntegerField(default=None, null=True)
    seat = models.IntegerField(default=None, null=True)
    studentInClass =models.ManyToManyField(User,blank=True,related_name="studentlist")

    status = models.CharField(
        max_length=4,
        choices=ans.choices,
        default=ans.free,
        )

    def __str__(self):
        return f"{self.subject_code} : {self.subject_name}"


