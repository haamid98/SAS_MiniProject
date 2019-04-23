from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserProfile, StudentInformation
from university.models import University
from Programs.models import Program
from applications.models import Application


@login_required(login_url='index')
def stuDash(request):
    # Get UserProfile & Information
    userProfile = get_object_or_404(UserProfile, user_id=User.objects.get(username=request.user.username).pk)
    stuInformation = get_object_or_404(StudentInformation, user_id=User.objects.get(username=request.user.username).pk)

    # Get Universities and their offered programs
    universities = University.objects.all()
    programs = Program.objects.all()

    # Get University Applications
    applications = Application.objects.filter(user_id=request.user.pk)

    context = {
        'userProfile': userProfile,
        'stuInformation': stuInformation,
        'universities': universities,
        'programs': programs,
        'applications': applications
    }

    return render(request, 'Dashboards/DashPartials/student.html', context)


@login_required(login_url='index')
def uniDash(request):
    # Get UserProfile
    userProfile = get_object_or_404(UserProfile, user_id=User.objects.get(username=request.user.username).pk)

    # Get staff's university programs
    programs = Program.objects.filter(university__title__exact=userProfile.university)

    # Get University Applications
    applications = Application.objects.filter(university__title__contains=userProfile.university)

    context = {
        'userProfile': userProfile,
        'programs': programs,
        'applications': applications
    }

    return render(request, 'Dashboards/DashPartials/universities.html', context)


@login_required(login_url='index')
def adminDash(request):
    # Get Universities and their programs offered
    universities = University.objects.all()
    programs = Program.objects.all()

    # Get University Staff
    uniStaff = UserProfile.objects.filter(userType='University Staff')

    context = {
        'universities': universities,
        'programs': programs,
        'staffs': uniStaff
    }

    return render(request, 'Dashboards/DashPartials/SAS.html', context)

