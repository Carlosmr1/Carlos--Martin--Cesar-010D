from django import forms
from .models import  User
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput(render_value=False))
    confirmar_contrasena = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            self.add_error('confirmar_contrasena', 'Las contraseñas no coinciden')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.contrasena = make_password(self.cleaned_data['contrasena'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['usuario', 'correo', 'contrasena']

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        email_validator = EmailValidator(message='El correo electrónico no es válido.')
        email_validator(correo)
        return correo
