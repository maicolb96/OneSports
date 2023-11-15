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
            post.save()

            return redirect('home')
    return render(request,'home.html',{'form':form})

def home(request):
    posts = Post.objects.all()[::-1]
    events = Events.objects.all()[::-1]
    comments = Comments.objects.all()
    likes = Likes.objects.all()
    post_likes = {}

    for post in posts:
        post_like_count = Likes.objects.filter(post=post).count()
        post_likes[post.id] = post_like_count

    context = {'posts':posts,
               'post_likes':post_likes,
               'comentarios':comments,
               'likes':likes,
               'events':events,
               }
    
    return render(request,'home.html',context)

@login_required
def edit_event(request,event_id):
    event = get_object_or_404(Events, pk=event_id)
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=event)
        form.save()
        return redirect('home')
    else:
        event = get_object_or_404(Events, pk=event_id)
        form = EventsForm(request.POST, request.FILES, instance=event)
        return render (request, 'layouts/partials/editar_eventos.html', {
            'event': event,
            'form': form
        })

@login_required
def delete_event(request,event_id):
    event = get_object_or_404(Events, pk=event_id)
    event.delete()
    return redirect('home')



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
    return render(request,'layouts/partials/login.html',{})

@login_required
def new_event(request):
    if request.method == 'POST':
        current_user = get_object_or_404(User, pk=request.user.pk)
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = current_user
            event.save()
            return redirect('home')
    return render(request,'layouts/partials/nuevo_evento.html',{})

def search_field_top(request,search_field):
    events= Events.objects.filter(description__incontains=search_field)[:3]
    post= Post.objects.filter(descripcion__incontains=search_field)[:3]
    users= User.objects.filter(username__incontains=search_field)[:3]
    groups= None
    context = {
        'eventos':events,
        'posts':post,
        'users':users,
        'groups':groups,
    }
    
    return render(request,'search.html',context)

def search_field_event():pass
def search_field_post():pass
def search_field_user():pass
