from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["knows_math", "knows_singing", "knows_music", "knows_drawing", "knows_video_editing", "knows_animation", "learn_math", "learn_singing", "learn_music", "learn_drawing", "learn_video_editing", "learn_animation", "description"]