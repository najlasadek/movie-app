from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['MovieTitle', 'Actor1Name', 'Actor2Name', 'DirectorName', 'MovieGenre', 'ReleaseYear']
