from django.urls import path
from . import views

urlpatterns = [
    path("", views.TechnologyList.as_view(
        template_name="quizzes/home.html"), name="home"),
    path("start-quiz/<int:id>", views.start_quiz,
         name="start-quiz"),  # technology id as parameter
    # path("subimtted-quiz/", views.validate_quiz, name="validate-quiz"),
    path("technologies/", views.TechnologyList.as_view(), name="technologies"),
    path("previous-quizzes/", views.quiz_history,
         name="previous-quizzes"),
    path("previous-quizzes/<int:id>", views.previous_quiz_detail,
         name="previous-quiz-detail"),
    path("add-technology/", views.AddTechnologyView.as_view(), name="add-technology"),
    path("questions/", views.QuestionsList.as_view(), name="questions"),
    path("add-question/", views.QuestionCreateView.as_view(), name="add-question"),
]
