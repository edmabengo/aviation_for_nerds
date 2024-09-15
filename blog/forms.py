# blog/forms.py
from django import forms

class UserExperienceForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    favorite_song = forms.CharField(label='Your Favorite Song', max_length=100)
