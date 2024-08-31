from django import forms
from .models import Technology, Questions


class AddTechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name']
        labels = {
            "name": "Technology Name",
        }


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'technology', 'answer', 'opt1', 'opt2', 'opt3']
        labels = {
            "question": "Question",
            "technology": "Technology",
            "answer": "Answer",
            "opt1": "Option 1",
            "opt2": "Option 2",
            "opt3": "Option 3",
        }

    def __init__(self, *args, **kwargs):
        super(AddQuestionForm, self).__init__(*args, **kwargs)
        self.fields['technology'].queryset = Technology.objects.all()


class StartQuizForm(forms.Form):
    # Overriding the answer field to display as radio buttons
    answer = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[]
    )  # Choices will be populated dynamically based on options

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)  # Pop the question from kwargs
        super(StartQuizForm, self).__init__(*args, **kwargs)

        if question:
            # Populating choices dynamically based on the question instance
            self.fields['answer'].choices = [
                (question.opt1, question.opt1),
                (question.opt2, question.opt2),
                (question.opt3, question.opt3),
                (question.answer, question.answer),
            ]
