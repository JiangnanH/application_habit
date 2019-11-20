from django import forms
from app_habit.models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'category', 'number', 'content']
