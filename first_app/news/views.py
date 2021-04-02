from django.shortcuts import render
from django.http import HttpResponse, Http404

from .forms import NewsModelForm
from news.models import News


# Create your views here.

def index(request, *args, **kwargs):
    qs = News.objects.all()
    context = {'news_list': qs}
    return render(request, 'index.html', context)

def detail_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404

    print(request.POST)
    print(request.GET)
    print(request.method == 'POST')
    print(request.method == 'GET')

    return render(request, 'news/detail.html', {'single_object': obj})

def test_view(request, *args, **kwargs):
    data = dict(request.GET)
    print(data)
    obj = News.objects.get(id=data['pk'][0])
    return HttpResponse(f'<b>{obj.article}</b>')

def create_view(request, *args, **kwargs):
    form = NewsModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        data = form.cleaned_data
        News.objects.create(**data)
    return render(request, 'forms.html', context)
    # if request.method == 'POST' and request.POST['article']:
    #     form = NewsForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data.get('article'))