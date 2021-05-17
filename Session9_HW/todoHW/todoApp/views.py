from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('deadline')
    
    return render(request, 'home.html', {'posts' : posts})

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
            author = request.user,
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method=='POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post': post})

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {
                'error': error
            })
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {
                'error': error
            })
        auth.login(request, found_user)
        return redirect('home')
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')

#ing
def mypage(request, user_pk):
    user = User.objects.get(pk=user_pk)

    return render(request, 'mypage.html', {'user' : user})

    