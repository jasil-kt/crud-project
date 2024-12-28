from django import forms

from cred_app.models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:

        model = Todo
        fields = "__all__"