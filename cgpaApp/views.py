from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout


GRADE_POINTS = {'S': 10, 'A+':9, 'A': 8, 'B': 7, 'C': 6, 'D': 5, 'F': 0, 'E':0}
@login_required(login_url='/login/')
def cal_cgpa(request):
    subjects = Subject.objects.all()
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)  # Save but don't commit to the database
            subject.user = request.user  # Assign the current user
            subject.save()
            return redirect('cal_cgpa')

    # Calculate CGPA
    total_credits = 0
    obtained_credits = 0

    for subject in subjects:
        total_credits += subject.credit
        obtained_credits += subject.credit * GRADE_POINTS.get(subject.grade, 0)

    if total_credits != 0:
        cgpa = obtained_credits / total_credits
    else:
        cgpa = 0

    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }

    return render(request, 'Home.html', context)

@login_required(login_url='/login/')
def subj_edit(request, subject_id):
    xx = get_object_or_404(Subject, id=subject_id)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=xx)
        if form.is_valid():
            form.save()
            return redirect('cal_cgpa')
    else:
        form = SubjectForm(instance=xx)

    context = {
        'form': form,
        'subject_id': subject_id,
    }

    return render(request, 'subj_edit.html', context)

@login_required(login_url='/login/')
def subj_delete(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    return redirect('cal_cgpa')

@login_required(login_url='/login/')
def result(request):
    subjects = Subject.objects.all()
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cal_cgpa')

    # Calculate CGPA
    total_credits = 0
    obtained_credits = 0

    for subject in subjects:
        total_credits += subject.credit
        obtained_credits += subject.credit * GRADE_POINTS.get(subject.grade, 0)

    if total_credits != 0:
        cgpa = obtained_credits / total_credits
    else:
        cgpa = 0

    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }

    return render(request, 'pdf.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check for username exists/not
        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            messages.error(request, "Username not found")
            return redirect('/login/')

        # Authenticate the user
        user_obj = authenticate(username=username, password=password)  
        if user_obj:
            login(request, user_obj)
            return redirect('cal_cgpa') 
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
    
    return render(request, "login.html")

#register as new
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")


#logout
def custom_logout(request):
    logout(request)
    return redirect('login')