import os
# Agar aap Google Gemini ya koi aur AI API use kar rahe hain toh uska client yahan import karein

def generate_interview_questions(job_role, experience_level, skills):
    # Yahan AI API ko request bhej kar questions generate karne ka code aayega
    # Maslan: 
    prompt = f"Generate 5 interview questions for a {experience_level} {job_role} with skills: {skills}"
    
    # Dummy list taaki abhi testing ho sake (baad mein AI API se connect kar lenge)
    questions = [
        f"Tell me about your experience as a {job_role}.",
        f"How do you handle challenging tasks related to {skills}?",
        "Describe a time when you solved a complex technical problem.",
        "What are your core strengths in this domain?",
        "Where do you see yourself professionally in the next 3 years?"
    ]
    return questions

def evaluate_answer(question, user_answer):
    # Yahan AI user ke answer ko analyze karega aur feedback, score dega
    score = 8.5
    feedback = "Good structure and relevant technical knowledge, but try to add more specific examples."
    return {"score": score, "feedback": feedback}