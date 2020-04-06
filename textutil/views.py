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
    analyzed = djtext

    if removepunc == 'on':
        puncs = ''''~!@#$%^&*(),./<-_>?:""{}|;''[]\='''
        djtext=analyzed
        analyzed=""
        for char in djtext:
            if char not in puncs:
                analyzed += char

    if (fullcaps == 'on'):
        djtext=analyzed
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()

    if (removespace == 'on'):
        djtext=analyzed
        analyzed=""
        for idx,char in enumerate(djtext):
            if not (djtext[idx] == " " and djtext[idx+1] == " "):
                analyzed += char

    djtext=analyzed
    if (countchar == 'on'):
        analyzed += '\nTotal Characters : '+str(len(djtext))

    if (countword == 'on'):
        spaces=0
        for i in range(len(djtext)-1):
            if djtext[i]==' ' and djtext[i+1]!=' ':
                spaces+=1
        analyzed += '\nTotal Words : '+str(spaces+1)
    
    param = {'purpose' : 'Remove Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', param)










