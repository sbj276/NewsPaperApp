from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


# Create your views here.

class ArticleListView(ListView):
	model = Article
	template_name = 'article_list.html'

class UpdateArticleView(LoginRequiredMixin ,UpdateView):
	model = Article
	fields = ('title','body')
	template_name = 'article_update.html'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


class DetailArticleView(DetailView):
	model = Article
	template_name = 'article_detail.html'

class DeleteArticleView(LoginRequiredMixin,DeleteView):
	model = Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class ArtilceCreateView(LoginRequiredMixin,CreateView):
	model = Article
	fields = ('title','body')
	template_name = 'article_new.html'
	login_url = 'login'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
