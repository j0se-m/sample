from django import forms

from  djangoModelHpClass.models import HpStudents

class WanafunziForm(forms.ModelForm):
    class Meta:
        model =HpStudents
        fields= "__all__"