from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import UserProfile, StudentInformation


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        usertype = request.POST['userType']
        university = request.POST['university']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('index')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('index')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    # create user profile to store specific user details and their user type
                    if usertype == 'University Staff':
                        userProfile = UserProfile(userType=usertype, university=university, user_id=User.objects.get(username=username).pk)
                        userProfile.save()
                    elif usertype == 'Student':
                        userProfile = UserProfile(userType=usertype, user_id=User.objects.get(username=username).pk)
                        stuInfo = StudentInformation(user_id=User.objects.get(username=username).pk)
                        userProfile.save()
                        stuInfo.save()

                    messages.success(request, 'You are now registered and can log in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'LandingSite/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        userProfile = get_object_or_404(UserProfile, user_id=User.objects.get(username=username).pk)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')

            if userProfile.userType is None:
                return redirect('adminDash')
            else:
                if userProfile.userType == 'Student':
                    return redirect('stuDash')
                elif userProfile.userType == 'University Staff':
                    return redirect('uniDash')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'LandingSite/index.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def updateUserProf(request):

    # retrieve user's profile and their student Information
    account = get_object_or_404(UserProfile, user_id=User.objects.get(username=request.user).pk)
    accInformation = get_object_or_404(StudentInformation, user_id=User.objects.get(username=request.user).pk)

    if request.method == 'POST':
        # filepath = request.FILES['filepath'] if 'filepath' in request.FILES else filepath
        account.profilePic = request.FILES['profPic'] if 'profPic' in request.FILES else account.profilePic
        account.save()

        accInformation.certificate_of_study = request.FILES['certificate_of_study'] if 'certificate_of_study' in request.FILES else accInformation.certificate_of_study
        accInformation.transcript = request.FILES['transcript'] if 'transcript' in request.FILES else accInformation.transcript

        accInformation.year_of_completion = request.POST['Year of Completion']
        accInformation.previousSchool = request.POST['previous School']
        accInformation.highest_level_of_study = request.POST['Level of Study']
        accInformation.DateOfBirth = request.POST['DateOfBirth']
        accInformation.gender = request.POST['gender']
        accInformation.nationality = request.POST['nationality']
        accInformation.nationalID = request.POST['nationalID']
        accInformation.address = request.POST['address']
        accInformation.city = request.POST['city']
        accInformation.state = request.POST['state']
        accInformation.zipcode = request.POST['zipcode']
        accInformation.phone_number = request.POST['phone number']
        accInformation.save()
        messages.success(request, 'Profile Updated')
    else:
        messages.info(request, 'No changes were made to your profile')

    return redirect('stuDash')
