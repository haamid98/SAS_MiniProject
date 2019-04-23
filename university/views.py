from .models import University
from django.contrib import messages
from django.shortcuts import redirect  # get_object_or_404


def regUni(request):
    if request.method == 'POST':
        Uni = University(title=request.POST['title'], address=request.POST['address'], city=request.POST['city'],
                         state=request.POST['state'], zipcode=request.POST['zipcode'],
                         phone_number=request.POST['phone_number'], website=request.POST['website'],
                         photo_main=request.FILES['photo_main'] if 'photo_main' in request.FILES else None, photo_logo=request.FILES['photo_logo']if 'photo_logo' in request.FILES else None,
                         description=request.POST['description'])
        Uni.save()

        messages.success(request, 'University Successfully Registered')
        return redirect('adminDash')
