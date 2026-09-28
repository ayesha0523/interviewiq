from django.shortcuts import render
from django.http import JsonResponse
from .ai_service import generate_interview_questions, evaluate_answer
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_questions_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            job_role = data.get('job_role', 'Software Engineer')
            experience_level = data.get('experience_level', 'Beginner')
            skills = data.get('skills', 'Python, Django')

            # AI service se questions generate karwana
            questions = generate_interview_questions(job_role, experience_level, skills)
            
            return JsonResponse({'status': 'success', 'questions': questions})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def evaluate_answer_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', '')
            user_answer = data.get('user_answer', '')

            # AI service se answer evaluate karwana
            result = evaluate_answer(question, user_answer)
            
            return JsonResponse({'status': 'success', 'evaluation': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
from .ai_service import convert_speech_to_text

@csrf_exempt
def speech_to_text_view(request):
    if request.method == 'POST':
        try:
            audio_file = request.FILES.get('audio')
            if not audio_file:
                return JsonResponse({'status': 'error', 'message': 'No audio file provided'}, status=400)

            text = convert_speech_to_text(audio_file)
            return JsonResponse({'status': 'success', 'text': text})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

