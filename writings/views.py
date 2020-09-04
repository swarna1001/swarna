from django.http import HttpResponse
from django.shortcuts import render
from .models import Writing


# Create your views here.

def writings_list(request):
    writings = Writing.objects.all().order_by('date')
    return render(request, 'writings/writings_list.html', {'writings': writings})


def writings_detail(request, slug):
    #return HttpResponse(slug)
    writing = Writing.objects.get(slug=slug)
    return render(request, 'writings/writing_detail.html', {'writing': writing})
