from django.shortcuts import render


# Create your views here.

def writings_list(request):
    return render(request, 'writings/writings_list.html')
