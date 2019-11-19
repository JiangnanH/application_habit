from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from app_habit.models import Article
from app_habit.forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    article_list = Article.objects.order_by('-date_time')
    context = {
        'article_list': article_list,
    }
    return render(request, 'app_habit/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def add_habit(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'app_habit/form.html',context)

@require_POST
def submit_habit(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect(reverse('habit:Home'))
    context = {
        'form': form,
    }
    return render(request, 'app_habit/form.html', context=context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request):
    article = get_object_or_404(Article)
    try:
        selected_choice = article.article_list.get(pk=request.POST['article'])
    except (KeyError, Article.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'habit:detail.html', {
            'article': article,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.number += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('habit:Home', args=(article.id,)))
