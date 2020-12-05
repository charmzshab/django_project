from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Lukyamuzi Shaban',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'December 05 , 2020'
    },
    {
        'author':'Tana Shakira',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'December 04 , 2020'
    },
    {
        'author':'Nassembwa Shadiya',
        'title':'Blog Post 3',
        'content':'Third post content',
        'date_posted':'December 03 , 2020'
    },
    {
        'author':'Kakooza Ibrahim',
        'title':'Blog Post 4',
        'content':'Fourth post content',
        'date_posted':'December 02 , 2020'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})