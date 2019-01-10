from rest_framework import generics

from article import models
from . import serializers

# Create your views here.

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

  # def get(self, request, *args, **kwargs):
  #    return self.list(request, *args, *kwargs)

  # def post(self, request, *args, **kwargs):
  #   return self.create(request, *args, **kwargs)

  # def get(self, request):
  #   articles = Article.objects.all()
  #   serializer = ArticleSerializer(articles, many=True)
  #   return Response({"articles": serializer.data})

  # def post(self, request):
  #   article = request.data.get('article')

  #   # Create an article from the above data
  #   serializer = ArticleSerializer(data=article)
  #   if serializer.is_valid(raise_exception=True):
  #     article_saved = serializer.save()
  #   return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

  # def put(self, request, pk):
  #   saved_article = get_object_or_404(Article.objects.all(), pk=pk)
  #   data = request.data.get('article')
  #   serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
  #   if serializer.is_valid(raise_exception=True):
  #     article_saved = serializer.save()
  #   return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

  # def delete(self, request, pk):
  #   # Get object with this pk
  #   article = get_object_or_404(Article.objects.all(), pk=pk)
  #   article.delete()
  #   return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)


