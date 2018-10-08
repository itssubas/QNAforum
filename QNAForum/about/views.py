from django.shortcuts import render, redirect
from about import forms
from django.contrib import messages

def about(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thanks for your feedback!')
            return redirect('index')

    else:
        form = forms.FeedbackForm()
        return render(request, 'about.html', {'form':form})
