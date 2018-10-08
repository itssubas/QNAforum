from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    asked_date = models.DateTimeField(auto_now_add=True)
    question_edited_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    tag_on = models.ForeignKey(Questions, on_delete=models.CASCADE, related_query_name='tag')

    def __str__(self):
        return self.name

class Answers(models.Model):
    answered_to = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    answered_date = models.DateTimeField(auto_now_add=True)
    answer_edited_date = models.DateTimeField(auto_now=True, blank=True)
    answer = models.TextField()

    def __str__(self):
        ans_preview = self.answer[0:40] + '...'
        return ans_preview
