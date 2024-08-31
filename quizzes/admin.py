from django.contrib import admin
from .models import Technology, Questions, QuizHistory, QuizHistoryQuestions
# Register your models here.


class QuizHistoryQuestionsAdmin(admin.ModelAdmin):
    readonly_fields = ('quiz', 'question', 'answer', 'user_answer')


admin.site.register(Technology)
admin.site.register(Questions)
admin.site.register(QuizHistory)
admin.site.register(QuizHistoryQuestions, QuizHistoryQuestionsAdmin)
