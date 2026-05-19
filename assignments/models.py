from django.db import models
from django.contrib.auth.models import AbstractUser
import json

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    model_answer = models.TextField(help_text="The ideal answer for semantic similarity comparison.")
    keywords = models.JSONField(default=list, help_text="List of keywords that should be present in the answer.")
    max_points = models.FloatField(default=100.0)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name="assignments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rubric(models.Model):
    assignment = models.OneToOneField(Assignment, on_delete=models.CASCADE, related_name='rubric')
    semantic_weight = models.FloatField(default=0.6, help_text="Weight for semantic similarity (e.g. 0.6 for 60%)")
    grammar_weight = models.FloatField(default=0.2, help_text="Weight for grammar correctness (e.g. 0.2 for 20%)")
    keyword_weight = models.FloatField(default=0.2, help_text="Weight for keyword presence (e.g. 0.2 for 20%)")

    def __str__(self):
        return f"Rubric for {self.assignment.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'}, related_name='submissions')
    submission_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username}'s submission for {self.assignment.title}"

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name='grade')
    semantic_score = models.FloatField(null=True, blank=True)
    grammar_score = models.FloatField(null=True, blank=True)
    keyword_score = models.FloatField(null=True, blank=True)
    final_score = models.FloatField(null=True, blank=True)
    feedback_json = models.JSONField(default=dict, blank=True)
    teacher_override_score = models.FloatField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    @property
    def effective_score(self):
        if self.teacher_override_score is not None:
            return self.teacher_override_score
        return self.final_score

    def __str__(self):
        return f"Grade for {self.submission}"
