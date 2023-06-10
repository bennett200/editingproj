from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'date_to_send': ('''Date to be sent(YYYY-MM-DD)''')
        }
        
