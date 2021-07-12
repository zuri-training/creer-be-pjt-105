from rest_framework import fields, serializers
from authentication.models import User
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['title', 'body', 'image']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['upvotes', 'answer_text']
