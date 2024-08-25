from django import forms
from .models import Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "date_of_admission", "isbn"]
        widget = {
            "admission_date": forms.DateInput(attrs={"type":"date"}),
        }

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateField(blank=False)
    email = forms.EmailField(blank=False)   