from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView

from posts.forms import CommentModelForm
from posts.models import PostModel
from django.views.generic import DetailView


class PostListView(ListView):
    template_name = 'blog.html'
    paginate_by = 2

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')

        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)
        return qs


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel


class CommentCreateView(CreateView):
    # template_name = 'blog-details.html'
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs['pk']})
