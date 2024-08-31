from django.utils import timezone
import random
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from .forms import AddTechnologyForm, AddQuestionForm, StartQuizForm
from .models import Technology, Questions, QuizHistory, QuizHistoryQuestions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden, HttpResponse
# Create your views here.


class AddTechnologyView(LoginRequiredMixin, FormView):
    template_name = 'quizzes/add_technology.html'
    form_class = AddTechnologyForm
    success_url = '/technologies'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Listing Technologies Class with a 'ListView'
class TechnologyList(LoginRequiredMixin, ListView):
    template_name = "quizzes/technologies.html"
    model = Technology
    context_object_name = "technologies"


# Listing Questions Class with a 'ListView'
class QuestionsList(LoginRequiredMixin, ListView):
    template_name = "quizzes/all_questions.html"
    model = Questions
    context_object_name = "questions"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

# Add a new Question Class based view


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Questions
    form_class = AddQuestionForm
    template_name = 'quizzes/add_question.html'
    success_url = reverse_lazy('questions')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


def start_quiz(request, id):
    technology = Technology.objects.get(pk=id)
    if request.method == 'POST':
        try:

            questions = Questions.objects.filter(technology=technology)
            correct = 0
            incorrect = 0
            attempted_questions = []
            for q in questions:
                if request.POST.get(str(q.id)) is None:
                    continue
                attempted_questions.append(
                    {"question": q.question, "answer": q.answer, "user_answer": request.POST.get(str(q.id))})
                if q.answer == request.POST.get(str(q.id)):
                    correct += 1
                else:
                    incorrect += 1
            print("Ques: ", attempted_questions)
            context = {
                'total_correct': correct,
                'total_incorrect': incorrect,
                'attempted_questions': attempted_questions
            }

            # Saving a quiz result
            quiz = QuizHistory.objects.create(
                user=request.user,
                technology=technology,
                score=correct,
                time=timezone.now()
            )
            quiz.save()

            # Saving questions for a perticular quiz
            for q in questions:
                if request.POST.get(str(q.id)) is None:
                    continue
                ques_answers = QuizHistoryQuestions.objects.create(
                    quiz=quiz,
                    question=q,
                    answer=q.answer,
                    user_answer=request.POST.get(str(q.id))
                )
                ques_answers.save()
            return render(request, 'quizzes/quiz_ended.html', context)
        except Exception as e:
            return HttpResponse(e)
    else:
        questions = list(Questions.objects.filter(technology=technology))
        random_questions = random.sample(questions, 2)
        return render(request, 'quizzes/start_quiz.html', {'questions': random_questions, 'technology': technology})


class QuizHistoryView(LoginRequiredMixin, ListView):
    model = QuizHistory
    template_name = "quizzes/quiz_history.html"
    context_object_name = "previous_quizzes"


def quiz_history(request):
    if not request.user.is_teacher:
        previous_quizzes = QuizHistory.objects.filter(user=request.user)
    else:
        previous_quizzes = QuizHistory.objects.all()
    return render(request, 'quizzes/quiz_history.html', {'previous_quizzes': previous_quizzes})


def previous_quiz_detail(request, id):
    quiz = QuizHistory.objects.get(pk=id)
    questions = QuizHistoryQuestions.objects.filter(quiz=quiz)
    if request.user == quiz.user or request.user.is_teacher:
        return render(request, 'quizzes/quiz_history_detail.html', {'questions': questions, 'quiz': quiz})
    else:
        raise Http404('Unauthorized!!')
