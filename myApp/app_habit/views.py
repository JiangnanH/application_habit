from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from app_habit.models import Habit
from app_habit.forms import HabitForm
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    habit_list = Habit.objects.order_by('-date_time')
    context = {
        'habit_list': habit_list,
    }
    return render(request, 'app_habit/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def add_habit(request):
    form = HabitForm()
    context = {
        'form': form,
    }
    return render(request, 'app_habit/form.html',context)

@require_POST
def submit_habit(request):
    form = HabitForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect(reverse('habit:Home'))
    context = {
        'form': form,
    }
    return render(request, 'app_habit/form.html', context=context)
