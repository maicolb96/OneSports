from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from SportBlog.models import *
from SportBlog.forms import *
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter #Se agrego para saltar la confirmación de google
# Create your views here.

@login_required
def new_post(request):
    form = PostForm(request.POST, request.FILES)
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            print(form.cleaned_data)
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('home')
    return render(request,'newpost.html',{'form':form})

def home(request):
    posts = Post.objects.all()
    posts = posts[::-1]
    post_likes = {}

    for post in posts:
        post_like_count = Likes.objects.filter(post=post).count()
        post_likes[post.id] = post_like_count
    context = {'posts':posts,
               'post_likes':post_likes,
               'comentarios':Comments.objects.all(),
               'likes':Likes.objects.all(),}
    return render(request,'home.html',context)

@login_required
def likeordislike(request,id_post):
    post_like = Likes()
    post_like.post = Post.objects.get(id=id_post)
    post_like.user = get_object_or_404(User, pk=request.user.pk)
    post_like.save()
    return redirect('home')

@login_required
def newcomentario(request,id_post):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        if request.POST.get('comentario'):
            comentario = Comments()
            comentario.user = current_user
            comentario.post = Post.objects.get(id=id_post)
            comentario.comentario = request.POST.get('comentario')
            comentario.save()
    return redirect('home')

def registro(request):
  return render(request,'layouts/partials/registro.html',{})

def ingreso(request):
    pass
