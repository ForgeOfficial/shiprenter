from django import forms

class RegisterForm(forms.Form):
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

    email = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'email',
            'name': 'email',
            'type': 'email',
            'class': 'w-full px-4 py-3 rounded-lg focus:outline-none text-sm',
            'placeholder': 'nom@example.com',
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
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password2',
            'name': 'password2',
            'type': 'password',
            'class': 'w-full px-4 py-3 rounded-lg focus:outline-none text-sm',
            'placeholder': '••••••••••',
            'required': 'required'
        })
    )