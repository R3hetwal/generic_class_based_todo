from django import forms
from users.models import NewUser
from django.forms import ModelForm
from django.core.validators import ValidationError, RegexValidator
import string
import random
import re

def validate_email_domain(email):
    domain = email.split('@')[-1]
    allowed_domains = ['gmail.com', 'hotmail.com', 'yahoo.com']

    if domain not in allowed_domains:
        raise ValidationError(f'Email domain {domain} is not allowed. Please use an email from one of these domains: {", ".join(allowed_domains)}')

# def validate_alphanumeric_password(password):
#     if not re.search('[a-z][A-Z][0-9][$@#$%&]', password):
#         raise forms.ValidationError('Password must be alphanumeric and contain special characters')

    
def validate_password_length(password):
    min_length = 8
    
    if len(password) < min_length:
        raise ValidationError(
            ("This password must contain at least 8 characters."),
                code='password_too_short'
        )

class LoginForm(forms.Form):
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput) 
    email = forms.EmailField(validators=[validate_email_domain])
    password = forms.CharField(widget=forms.PasswordInput) 


class SignupForm(forms.ModelForm):
    first_name = forms.CharField()
    # GENDER_CHOICES = [
    # ('M', 'Male'), ('F', 'Female'), ('O', 'Others')
    # ]
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    password = forms.CharField(validators=[validate_password_length], widget=forms.PasswordInput)
    password2 = forms.CharField(validators=[validate_password_length], widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = NewUser
        fields = ['email', 'username']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        domain = email.split('@')[-1]
        allowed_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']

        if domain not in allowed_domains:
            raise ValidationError(f'Email domain {domain} is not allowed. Please use an email from one of these domains: {", ".join(allowed_domains)}')
        return email


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        # if not re.search('[a-z][A-Z][0-9][$@#$%&]', password):
        #     raise forms.ValidationError('Password must be alphanumeric and contain special characters')
    

        min_length = 8
        if len(password2) < min_length:  # and not re.search("[a-z]", password) and not re.search("[A-Z]", password) and not re.search("[@!#$%&^*]", password) and not re.search("[0-9]", password):
            raise ValidationError(
                ("The password must contain at least 8 characters."),
                # ('The password should contain atleast one lowercase, one uppercase and alphanumeric values.'),
                # ('The password should also contain special characters as !, @, #, %, &, *, $, ^.')
                code='password_too_short'
            )
        
        elif not re.search("[a-z]", password):
            raise ValidationError('Password should contain lowercase characters')
        
        elif not re.search("[A-Z]", password):
            raise ValidationError('Password should contain uppercase characters')

        elif not re.search("[@!#$%&^*]", password):
            raise ValidationError('Password should contain special characters')
        
        elif not re.search("[0-9]", password):
            raise ValidationError('Password should contain numeric value')
        
        else:
            print('Password Validated!')
        

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match')

        return password2
        