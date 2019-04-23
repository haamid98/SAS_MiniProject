from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserProfile
from university.models import University


def index(request):

    uniList = University.objects.all()

    context = {
        'uniList': uniList
    }

    if request.user.is_authenticated:

        userProfile = get_object_or_404(UserProfile, user_id=User.objects.get(username=request.user.username).pk)

        if userProfile.userType is None:
            return redirect('adminDash')
        else:
            if userProfile.userType == 'Student':
                return redirect('stuDash')
            elif userProfile.userType == 'University Staff':
                return redirect('uniDash')
    else:
        return render(request, 'LandingSite/index.html', context)
