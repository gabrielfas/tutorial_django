from django.shortcuts import render
from django.utils import timezone
from .models import Post

from rest_framework import viewsets
from .serializers import PostModelSerializers, AuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = PostModelSerializers
    queryset = Post.objects.all().order_by('-title')

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES