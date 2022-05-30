from django import forms
from django.contrib.auth.models import User
from . import models


class AdminSigupForm(forms.ModelForm):
    def clean_email(self):
        demail = self.cleaned_data['email']
        if "sggs.ac.in" not in demail:
            raise forms.ValidationError("You must be use sggs.ac.in Email ID")
            message = "You already Booked the Room One can Book Only one Room"
            messages.error(request, message)
            return redirect('register_page')
        return demail
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['profile_pic','roll','branch','cl','mobile','fee','email','status','gender','Nationality','category','country','state','city','village']

        



class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary','mobile','status','branch1','teacher_profile']





presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()




#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'



#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class Upload_DocumentForm(forms.ModelForm):
    class Meta:
        model=models. Upload_Document
        fields=['student','tc','mark10','mark12','g_certificate']




