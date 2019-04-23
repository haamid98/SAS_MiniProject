from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Application
from university.models import University
from Programs.models import Program
from accounts.models import UserProfile, StudentInformation


def applyUni(request):
    if request.method == 'POST':

        application = Application(user=get_object_or_404(User, id=request.user.pk), studentProf=get_object_or_404(UserProfile, user_id=User.objects.get(username=request.user.username).pk), studentInfo=get_object_or_404(StudentInformation, user_id=User.objects.get(username=request.user.username).pk), university=get_object_or_404(University, id=request.POST['University']), program=get_object_or_404(Program, id=request.POST['Program']), progress=0, is_approved=False)
        application.save()

        messages.success(request, 'You Application was Submitted Successfully!')
        return redirect('stuDash')


def delApplication(request):
    if request.method == 'POST':

        # Get application object from database based on parameter from post request
        application = Application.objects.filter(id=request.POST['Application ID'])
        # Delete Application object from database
        application.delete()

        messages.success(request, 'Your Application was Cancelled Successfully!')
        return redirect('stuDash')


def updateProgress(request):
    if request.method == 'POST':
        # Get application object from database based on parameter from post request
        applicationID = request.POST['Application ID']
        application = get_object_or_404(Application, id=applicationID)

        # Update student application progress
        application.progress = float(request.POST['Progress']) if 'Progress' in request.POST else application.progress
        application.is_approved = bool(request.POST['is_Approved']) if 'is_Approved' in request.POST else False

        application.save()

        messages.success(request, 'Student Application Progress Updated Successfully!')
        return redirect('uniDash')
