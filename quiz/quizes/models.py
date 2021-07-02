
from django.db import models
import random

# Create your models here.
DIFF_ChOISE ={
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
}

class Quiz(models.Model):
    name = models.CharField(max_length=130)
    topic = models.CharField(max_length=130)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="requied score in percentage")
    difficulty = models.CharField(max_length=6,choices=DIFF_ChOISE)

    def __str__(self) -> str:
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        questions = self.question_set.all()
        random.shuffle(questions)
        return questions[:self.number_of_questions]
        
