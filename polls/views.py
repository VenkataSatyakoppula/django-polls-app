from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question
from .serialize import QuestionSerializer, AnswerSerializer
from rest_framework.parsers import FormParser,MultiPartParser

from polls import serialize

class QuestionCreateAPIView(APIView):
    parser_classes = [FormParser,MultiPartParser]
    
    def get(self,request,format=None):
        all_questions = Question.objects.all();
        serializer = QuestionSerializer(all_questions,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

