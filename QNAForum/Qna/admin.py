from django.contrib import admin
from Qna.models import Questions, Answers, Tag
# Register your models here
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Tag)
