from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Assignment, Submission, Grade, Rubric
from .ai.scoring_aggregator import evaluate_submission

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'assignments/login.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.role == 'teacher':
        return redirect('teacher_dashboard')
    elif request.user.role == 'student':
        return redirect('student_dashboard')
    else:
        return redirect('admin:index')

@login_required
def teacher_dashboard(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    assignments = Assignment.objects.filter(teacher=request.user).order_by('-created_at')
    
    return render(request, 'assignments/teacher_dashboard.html', {'assignments': assignments})

@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return redirect('dashboard')
    
    assignments = Assignment.objects.all().order_by('-created_at')
    submissions = Submission.objects.filter(student=request.user)
    submitted_assignment_ids = submissions.values_list('assignment_id', flat=True)
    
    context = {
        'assignments': assignments,
        'submitted_ids': submitted_assignment_ids,
        'submissions': submissions
    }
    return render(request, 'assignments/student_dashboard.html', context)
