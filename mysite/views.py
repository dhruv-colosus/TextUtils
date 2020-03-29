from django.http import HttpResponse
from django.shortcuts import render

def index(response):
    return render(response,"index.html")

def analyze(response):
    djtext=response.POST.get('text','default')    
    removepunc=response.POST.get('removepunc','off')
    capitalize=response.POST.get('capitalize','off')
    charcount=response.POST.get('charcount','off')
    
    
    if removepunc=="on":
        punctuations=''',./?!:;-(")_'/{}'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed+=char

        params={"Analyzed_text":analysed,"greetings": "Removing Punctuations..."}
        return render(response,"analyze.html",params)

    elif capitalize=="on":
        
        analysed=djtext.upper()
        params={"Analyzed_text":analysed,"greetings": "Capitalizing"}
        return render(response,"analyze.html",params)

    elif charcount=="on":
        analysed=0
        for char in djtext:
            analysed+=1
        params={"Analyzed_text":analysed,"greetings": "Counting Characters"}
        return render(response,"analyze.html",params)

        
    else:
       return HttpResponse("Error Boi")


