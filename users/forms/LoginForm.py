from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'type': 'text',
            'class': 'w-full px-4 py-3 rounded-lg focus:outline-none text-sm',
            'placeholder': 'Username',
            'required': 'required'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'type': 'password',
            'class': 'w-full px-4 py-3 rounded-lg focus:outline-none text-sm',
            'placeholder': '••••••••••',
            'required': 'required'
        })
    )