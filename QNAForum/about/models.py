from django.db import models

class Feedback(models.Model):
    your_name = models.CharField(max_length=30)
    your_email = models.EmailField(blank=True)
    your_message = models.CharField(max_length=2000)
    your_feedback_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.your_name
