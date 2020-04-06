# this file is made by me- akash
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('intext', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    removespace = request.POST.get('removespace', 'off')
    countchar = request.POST.get('countchar', 'off')
    countword = request.POST.get('countword', 'off')
    analyzed = " "

    if removepunc == 'on':
        puncs = '''~!@#$%^&*(),./<-_>?:""{}|;''[]\='''
        for char in djtext:
            if char not in puncs:
                analyzed += char

    elif (fullcaps == 'on'):
        for char in djtext:
            analyzed+=char.upper()

    elif (removespace == 'on'):
        for idx,char in enumerate(djtext):
            if not (djtext[idx] == " " and djtext[idx+1] == " "):
                analyzed += char

    elif (countchar == 'on'):
        analyzed='Total Characters : '+str(len(djtext))

    elif (countword == 'on'):
        analyzed = 'Total Words : '+str(djtext.count(' '))
    
    param = {'purpose' : 'Remove Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', param)










