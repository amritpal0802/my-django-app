from django import forms
class StudentForm(forms.Form):
    firstname=forms.CharField(label="enter first name",max_length=50)
    lastname=forms.CharField(label="enter last name",max_length=50)
    file=forms.FileField()
