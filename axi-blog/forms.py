from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email. Please don't use .edu.")
        return email

class UserFrorm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ['username', 'email', 'password']

