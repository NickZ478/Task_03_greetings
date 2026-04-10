from django import forms
from .models import UserName

class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-input',
                'placeholder': 'Введите ваше имя...',
                'id': 'name-input'
            })
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Пожалуйста, введите ваше имя!')
        return name.strip()