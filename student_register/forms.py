from django import forms
from .models import Student 


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        #fields = "__all__"
        fields = ('full_name', 'roll_number','mobile','position')
        label = {
            'full_name' : 'Full Name',
            'roll_number' :'Roll Number',
            'mobile' : 'Mobile', 
            'position': 'Position'
        }
    def __init__(self,*args,**kwargs): #this block of code gives select in dropdown
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"