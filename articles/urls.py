from django.urls import path
from .views import DetailArticleView,UpdateArticleView,DeleteArticleView,ArtilceCreateView,ArticleListView


urlpatterns = [
	path('',ArticleListView.as_view(),name='article_list'),
	path('new/',ArtilceCreateView.as_view(),name='article_new'),
	path('<int:pk>/edit/',UpdateArticleView.as_view(),name='article_update'),
	path('<int:pk>/',DetailArticleView.as_view(),name='article_detail'),
	path('<int:pk>/delete/',DeleteArticleView.as_view(),name='article_delete')
]