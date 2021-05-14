# This file is created by me- Anukul
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Anukul'}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse('This is about page of my website\n <a href="/">Go back</a>')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc=request.GET.get('removepunctuation','off')
    capall=request.GET.get('capitaliseall','off')
    capfirst=request.GET.get('capitalisefirst','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremove','off')
    charcount=request.GET.get('charactercounter','off')
    final=''
    punctuations=',./-_'
    if (removepunc=="on"):
        for char in djtext:
            if char not in punctuations:
                final = final+char 
        params={'func':'Punctuations removed successfully!','final':final}
        return render(request,'analyze.html',params)
    elif(capall=='on'):
        final = djtext.upper()
        params={'func':'Capitalised All successfully!','final':final}
        return render(request,'analyze.html',params)
    elif(capfirst=='on'):
        for index,char in enumerate(djtext):
            if index==0:
                final = final + char.upper()
            else:
                final = final + char
        params={'func':'Capitalised first Character successfully!','final':final}
        return render(request,'analyze.html',params)
    elif(newlineremover=='on'):
        for char in djtext:
            if char!='\n':
                final=final+char
        params={'func':'New lines removed successfully!','final':final}
        return render(request,'analyze.html',params)
    elif(extraspaceremover=='on'):
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                final=final+char
        params={'func':'Extra Spaces removed successfully!','final':final}
        return render(request,'analyze.html',params)
    elif(charcount=='on'):
        final = 0
        for char in djtext:
            final+=1
        params={'func':'Characters Counted successfully!','final':final}
        return render(request,'analyze.html',params)
    else:
        params={'final':'Error in retrieving data'}
        return render(request,'analyze.html',params)

def readfile(request):
    path = f"D:\Coding\django\\firstProject\\readme.txt"
    f=open(path,'rb')
    content = f.read()
    return HttpResponse(content)
# import os
# print(os.path.abspath("readme.txt"))