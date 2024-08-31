from django.db import models
from users.models import CustomUser
# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Questions(models.Model):
    question = models.TextField(max_length=500)
    technology = models.ForeignKey(
        Technology, on_delete=models.CASCADE, related_name="technology")
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    opt1 = models.CharField(max_length=500)
    opt2 = models.CharField(max_length=500)
    opt3 = models.CharField(max_length=500)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Questions"


class QuizHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quiz History"

    def __str__(self):
        return f"Quiz id: {self.id} - {self.user.first_name}'s quiz on {self.technology}"


class QuizHistoryQuestions(models.Model):
    quiz = models.ForeignKey(QuizHistory, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500, default='')
    user_answer = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Quiz History Questions"

    def __str__(self):
        return f"Quiz id: {self.quiz.id} - {self.question.question}"
