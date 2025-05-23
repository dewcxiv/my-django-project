from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def home(request):
    posts = Post.objects.all()
    output = ""
    for post in posts:
        output += f"<h2>{post.title}</h2><p>{post.content}</p><hr>"
    return HttpResponse(output)

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            Post.objects.create(title=title, content=content)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Title and content cannot be empty.")
    return render(request, "create_post.html")
