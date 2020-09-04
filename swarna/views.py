from django.shortcuts import render, HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
    #return HttpResponse('homepage')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse('about')
