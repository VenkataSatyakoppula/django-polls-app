from django.http import HttpResponse,JsonResponse
from .models import Question
from .serialize import QuestionSerializer
from django.http import JsonResponse

def list_questions(request):
    questions = Question.objects.all()
    q_serialer = QuestionSerializer(questions,many=True)
    return JsonResponse(q_serialer.data,safe=False)

def hello_view(request):
        return HttpResponse("Hello")

