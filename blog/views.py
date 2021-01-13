from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    keyword = request.GET.get('keyword')

    if keyword:
        posts = Post.objects.filter(
                 Q(title__icontains=keyword) | Q(material__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['blogs'] = Post.objects.all()[:3]
       return context
