from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Game,Profile,News,Comment
from .email import *
from .forms import CommentForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import


# Create your views here.
def index(request):
    games = Game.objects.all()
    news = News.objects.all()

    return render(request,'index.html',{"games":games,"news":news})

def games(request):

    return render(request,'games.html')

def trailers(request):
    trailers = Game.objects.all()

    return render(request,'trailers.html',{'trailers':trailers})

def news(request):

    return render(request,'news.html')

@login_required(login_url='/accounts/login/')
def article(request,id):
    current_user = request.user

    try:
        comments = Comment.objects.filter(review_id=id)
    except:
        comments=[]

    news = News.objects.get(id=id)
    profile = Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = profile
            comment.review = news
            comment.save()
    else:
        form = CommentForm()

    return render(request,'article.html',{"form":form,"news":news,"comments":comments})
