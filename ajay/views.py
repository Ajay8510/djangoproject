#i am created this video
from  django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def removepunc(request):
    string = request.POST.get('string','default')
    status = int(request.POST.get('status', 0))
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if status == 1:
        analyzed = ''
        for char in string:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed, 'purpose': 'Remove Punctuations'}
        return render(request, 'success.html', params)
    elif status == 2:
        analyzed = string.upper()
        params = {'analyzed_text': analyzed, 'purpose': 'in upper case'}
        return render(request, 'success.html', params)
    elif status == 3:
        analyzed = string.lower()
        params = {'analyzed_text': analyzed, 'purpose': 'in lower case'}
        return render(request, 'success.html', params)
    elif status == 4:
        analyzed = string.title()
        params = {'analyzed_text': analyzed, 'purpose': 'in title case'}
        return render(request, 'success.html', params)
    elif status == 5:
        analyzed = len(string)
        params = {'analyzed_text': analyzed, 'purpose': 'Length'}
        return render(request, 'success.html', params)
    else:
        return HttpResponse("Error: Please check the punctuations <a href='/'>Back</a>")







def capitalizefirst(request):
    return HttpResponse("<h1>capitalizefirst</h1> <a href='/'>Back</a>")

def newlineremove(request):
    return HttpResponse("<h1>newlineremove</h1> <a href='/'>Back</a>")

def spaceremove(request):
    return HttpResponse("<h1>spaceremove</h1> <a href='/'>Back</a>")


def charcount(request):
    return HttpResponse("<h1>charcount</h1> <a href='/'>Back</a>")

def about(request):
    return HttpResponse("<h1>Hi this is about page</h1> <a href='/'>Back</a>")