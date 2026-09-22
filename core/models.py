from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target_job_role = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=100) # e.g., Beginner, Mid, Senior
    skills = models.TextField(help_text="Comma-separated skills")
    
    def __str__(self):
        return f"{self.user.username} - {self.target_job_role}"

class InterviewSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=255)
    interview_type = models.CharField(max_length=100) # Technical, HR, Behavioral
    created_at = models.DateTimeField(auto_now_add=True)
    overall_score = models.FloatField(null=True, blank=True)
    report_summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Interview for {self.user.username} on {self.job_role} ({self.created_at})"

class InterviewQuestion(models.Model):
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    user_answer = models.TextField(null=True, blank=True)
    ai_feedback = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)