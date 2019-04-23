from .models import Program
from university.models import University
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404


def addProg(request):
    if request.method == 'POST':

        prog = Program(university=get_object_or_404(University, title=request.POST['university']), title=request.POST['title'], department=request.POST['department'], level=request.POST['level'], requirements=request.POST['requirements'], duration=float(request.POST['duration']), campus=request.POST['campus'], description=request.POST['description'])
        prog.save()
        messages.success(request, 'Program Saved Successfully')
        if request.user.username == 'SASadmin':
            return redirect('adminDash')
        else:
            return redirect('uniDash')
