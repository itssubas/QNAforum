from django.shortcuts import render, redirect
from Qna.models import Questions, Answers, Tag
from django.views.generic import CreateView
# from Qna.forms import AskQuestionForm, AddTags
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    questionlist = Questions.objects.all()
    #counting number of answers
    ans_count = []
    tags =[]
    # tags = [[] for _ in range(len(questionlist))]
    for val in range(1, len(questionlist)+1):
        ans_count.append(len(Answers.objects.filter(answered_to__id=val)))
        tags.append(Tag.objects.filter(tag_on__id=val))

    return render(request, 'index.html', {'qu':questionlist,'ans_count':ans_count, 'tags':tags})

def question_in_detail(request, pk):
    question = Questions.objects.get(id=pk)
    ans = Answers.objects.filter(answered_to__id=pk)
    tags = Tag.objects.filter(tag_on__id=pk)

    return render(request, 'details.html', {'object':question, 'ans':ans, 'tags':tags})

# @login_required
class AskQuestion(CreateView):
    model = Questions
    fields = ['title', 'description']
    template_name='questions_form.html'

    def form_valid(self, form):
        form.instance.asked_by = self.request.user
        return super().form_valid(form) 

# @login_required
# def ask_question(request):
#     if request.method == 'POST':
#         form = AskQuestionForm(request.POST)
#         form2 = AddTags(request.POST)
#         if form.is_valid() and form2.is_valid():
#             with_user = form.save(commit=False)
#             with_user.asked_by = request.user
#             tag_instance = form2.save(commit=False)
#             # tag_instance.tag_on = Questions.objects.get(form.cleaned_data['id'])
#             tag_instance.tag_on = with_user.id
#             with_user.save()
#             tag_instance.save()
#             messages.success(request, f'Your question is posted.')
#             return redirect('index')
#
#     else:
#         form = AskQuestionForm()
#         form2 = AddTags()
#     return render(request, 'questions_form.html', {'form':form, 'form2':form2})
