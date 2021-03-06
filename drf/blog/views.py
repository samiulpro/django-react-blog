from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Blog
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .serializer import BlogSerializer


# class BlogAPIView(APIView):
#     def get(self, request, format=None):
#         blog_list=Blog.objects.all()
#         blog_serializer = BlogSerializer(blog_list, many=True)
#         return Response(blog_serializer.data)

# class BlogListAPIView(APIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogCreateAPIView(CreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogRetrieveAPIView(RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogUpdateAPIView(UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
# if we use "id" instead of "pk" in url then we have to use here
#     lookup_field = "id"
#
# class BlogDestroyAPIView(DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogListCreateView(CreateModelMixin, ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class BlogDetailView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.put(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
#

# class BlogListCreateView(ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = [FormParser, MultiPartParser]
