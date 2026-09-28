from django.urls import path
from .views import get_questions_view, evaluate_answer_view,speech_to_text_view

urlpatterns = [
    path('api/generate-questions/', get_questions_view, name='generate_questions'),
    path('api/evaluate-answer/', evaluate_answer_view, name='evaluate_answer'),
    path('api/speech-to-text/', speech_to_text_view, name='speech_to_text'),
]
