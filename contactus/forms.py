from django import forms
from .models import ContactUs

class NewMessage(forms.ModelForm):

    name = forms.CharField(max_length=100,)
    subject = forms.CharField(max_length=400,)
    message = forms.CharField( widget=forms.Textarea(attrs={
        'rows':5,'placeholder':'What is the message'}
    ),
     max_length=5000,
     help_text='The max lenght is 5000'
    )
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter valid Email'}),
                                help_text='email like example@gmail.com'
                            )

    class Meta:
        model = ContactUs
        fields = ['name','subject','message','email']
