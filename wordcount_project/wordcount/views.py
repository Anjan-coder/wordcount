from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd

def home(request):
    return render(request,'home.html',{"hi":5555})
def about(request):
    return render(request,'about.html',{"hi":5555})

def count(request):
    t1=request.GET['fulltext']
    text=t1.split()
    cnt_len=len(text)
    d={}
    for i in text:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    df=pd.DataFrame(d)        

    return render(request,'count.html',{"user_text":t1,"txtcnt":cnt_len,"wordscount":d})
