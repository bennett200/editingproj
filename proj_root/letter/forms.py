from django import forms
from django.forms import Textarea, ModelForm

from .models import Letter, LetterUser, Friends

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
        labels = {
            'first_name': ('First Name(of recipiant)'),
            'last_name': ('Last Name(of recipiant)'),
            'date_to_send': ('''Date to be sent(YYYY-MM-DD)''')
        }
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
    class Media:
        css = {
            'all': ('form.css',)
        }

class LetterUserForm(ModelForm):
    class Meta:
        model = LetterUser
        fields = '__all__'
        labels = {
            'first_name': ('First Name'), 
            'last_name': ("Last Name"),
            'email': ('Email')
        }
    class Media:
        css = {
            'all': ('form.css',)
        }
        
        
class FriendsForm(ModelForm):
    class Meta:
        model = Friends
        fields = '__all__'
        labels = {
            'friend_nick': ('Nickname'),
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'email': ('Email'),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('friend_nick')
        if not nick:
            raise forms.ValidationError('Please Enter A Nickname')