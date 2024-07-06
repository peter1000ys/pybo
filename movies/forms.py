from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):

    class Meta:
        
        model = Movie
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'genre' : forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.5, 'min': 0, 'max': 5}),
        }   
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

