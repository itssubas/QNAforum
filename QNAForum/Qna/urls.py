from django.urls import path, re_path
from Qna.views import home, AskQuestion, question_in_detail

urlpatterns = [
    path('', home, name='index'),
    # path('question/<int:pk>/',views.MyDetailView.as_view(), name='question-detail'),
    path('question/<int:pk>/',question_in_detail, name='question-detail'),
    path('question/ask/',AskQuestion.as_view(), name='question-ask'),
]
