from django.db import models
from django.contrib.auth.models import User
from university.models import University
from Programs.models import Program
from accounts.models import UserProfile, StudentInformation


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studentProf = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    studentInfo = models.ForeignKey(StudentInformation, on_delete=models.DO_NOTHING)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    progress = models.FloatField(default=0.0, null=False)
    is_approved = models.BooleanField(default=False, null=False)

    # def __str__(self):
    #     #     return self.university, self.program
