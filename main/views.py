from django.shortcuts import render, redirect
from .models import ExamForm

def login_view(request):
    if request.method == 'POST':
        return redirect('/dashboard/')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def exam_form(request):
    if request.method == 'POST':
        ExamForm.objects.create(
            name=request.POST['name'],
            course=request.POST['course'],
            year=request.POST['year'],
            address=request.POST['address'],
            phone=request.POST['phone']
        )
        return redirect('/success/')
    return render(request, 'form.html')

def success(request):
    return render(request, 'success.html')