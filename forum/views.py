from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from forum.forms import CreateThread, CreatePost
from forum.models import Thread

# Create your views here.
def home_view(request):
    return redirect(forum_home)

def forum_home(request):
    threads = Thread.objects.all() 
    context = {
        'threads': threads
    }
    return render(request, 'forum/home.html', context=context)

@login_required
def create_thread(request):
    threadForm = CreateThread(data=request.POST or None)
    postForm = CreatePost(data=request.POST or None)
    context = {
        'threadForm': threadForm,
        'postForm': postForm
    }
    if threadForm.is_valid() and postForm.is_valid():
        thread = threadForm.save(commit=False)
        thread.creator = request.user
        thread.save()
        post = postForm.save(commit=False)
        post.title = thread
        post.creator = request.user
        post.save()
        threadForm = CreateThread()
        postForm = CreatePost()
        return redirect(home_view)
    return render(request, 'forum/create-thread.html', context=context)

def view_thread(request, id):
    thread = Thread.objects.get(id=id)
    if thread:
        posts = thread.post_set.all()
    context = {
        'thread': thread,
        'posts': posts
    }
    postForm = CreatePost(data=request.POST or None)
    if postForm.is_valid():
        post = postForm.save(commit=False)
        post.title = thread
        post.creator = request.user
        post.save()
        postForm = CreatePost()
    context['form'] = postForm
    return render(request, 'forum/view-thread.html', context=context)