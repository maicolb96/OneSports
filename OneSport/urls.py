"""
URL configuration for OneSport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('post/newpost', views.new_post,name = 'newpost'),
    path('comentario/newcomentario/<int:id_post>/', views.newcomentario,name='comment_new'),
    path('like/<int:id_post>/', views.likeordislike,name='likeordislike'),
    path('registro/',views.registro, name='registro'),
    path('new_event/',views.new_event, name='new_event'),
    path('editar_evento/<int:event_id>',views.edit_event, name='editar_evento'),
    path('borrar_evento/<int:event_id>',views.delete_event, name='borrar_evento'),
    path('login/',views.ingreso, name='ingreso'),
    path('',views.home,name='home'),
    path('search/top/<str:search_field>',views.search_field_top, name='search_field'),
    path('search/event/<str:search_field>',views.search_field_event, name='search_field'),
    path('search/post/<str:search_field>',views.search_field_post, name='search_field'),
    path('search/user/<str:search_field>',views.search_field_user, name='search_field'),
    path('search/group/<str:search_field>',views.search_field_group, name='search_field'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
