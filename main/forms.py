"""
Module with forms for main application
"""

from django import forms
from django.forms import Textarea
from main.models import MyTest, Card, Result, Comments



class CreateFormTest(forms.ModelForm):
    """
    class form created instance Test
    """

    class Meta:
        model = MyTest
        fields = ["name", "description"]


class CommentForm(forms.ModelForm):
    """
    class form created instance comments
    """

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 5})

    class Meta:
        model = Comments
        fields = ['text']


class CreateFormCard(forms.ModelForm): #TODO: сделать создание карты с помощью form_set
    """
    class form created instance Cart
    """

    def __init__(self, *args, **kwargs):
        super(CreateFormCard, self).__init__(*args, **kwargs)
        self.fields['test'].queryset = kwargs["initial"]["tests_queryset"]

    class Meta:
        model = Card
        fields = ['test', 'question', 'correct_answer', 'wrong_answer1',
                  'wrong_answer2', 'wrong_answer3']


class RunTestForm(forms.Form):   #TODO: Уменьшить зависимость :(
    def __init__(self, *args, **kwargs):
        super(RunTestForm, self).__init__(*args, **kwargs)

        for card in kwargs["initial"]['questions']:
            GEEKS_CHOICES = {
                ("1", f"{card.correct_answer}"),
                ("2", f"{card.wrong_answer1}"),
                ("3", f"{card.wrong_answer3}"),
                ("4", f"{card.wrong_answer2}"),
            }

            self.fields.update(
                {f"{card.question}": forms.ChoiceField(choices=GEEKS_CHOICES)})

    def clean(self):
        cleaned_data = super(RunTestForm, self).clean()
        count_correct_answer = 0
        count_questions = len(cleaned_data)
        for Key, value in cleaned_data.items():
            if value == '1':
                count_correct_answer += 1

        session = self.initial["request"].session
        session["result"] = count_correct_answer
        session["count"] = count_questions
        percent = count_correct_answer * 100 / count_questions
        session["percent"] = percent

        result = Result.objects.filter(user_id=self.initial["request"].user.id,
                                       test_id=self.initial["test"].id).first()

        if result:
            if count_correct_answer == count_questions:
                result.flag = True
                result.count += 1
                result.percent = percent

            else:
                result.count += 1
                if result.percent < percent:
                    result.percent = percent
            result.save()

        else:
            if count_correct_answer == count_questions:

                res = Result(
                    user=self.initial["request"].user,
                    test=self.initial["test"],
                    flag=True,
                    percent=percent
                )

            else:
                res = Result(
                    user=self.initial["request"].user,
                    test=self.initial["test"],
                    percent=percent,
                    count=1
                )

            Result.save(res)
