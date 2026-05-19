import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auto_grader.settings')
django.setup()

from assignments.models import CustomUser

# Create a teacher
teacher, created = CustomUser.objects.get_or_create(username='teacher')
if created:
    teacher.set_password('password123')
    teacher.role = 'teacher'
    teacher.save()
    print("Created teacher user.")

# Create a student
student, created = CustomUser.objects.get_or_create(username='student')
if created:
    student.set_password('password123')
    student.role = 'student'
    student.save()
    print("Created student user.")
