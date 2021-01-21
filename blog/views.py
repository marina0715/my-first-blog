from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q


def start(request):
    
    keyword = request.GET.get('keyword')

    if keyword:
        posts = Post.objects.filter(
                 Q(title__icontains=keyword) | Q(material__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'blog/start.html')
    

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
            post.image1 = request.FILES['image1']
            post.image2 = request.FILES['image2']
            post.image3 = request.FILES['image3']
            post.image4 = request.FILES['image4']
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
            post.image1 = request.FILES['image1']
            post.image2 = request.FILES['image2']
            post.image3 = request.FILES['image3']
            post.image4 = request.FILES['image4']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['blogs'] = Post.objects.all()[:3]
       return context

def category(request, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html',
                   {'category': category, 'posts': posts })


def post_calorie_low(request):
    posts = Post.objects.extra(select={'calorie': 'CAST(calorie AS INTEGER)'}).order_by('calorie')
    return render(request, 'blog/post_calorie_low.html',{'posts': posts})

def post_calorie_high(request):
    posts = Post.objects.extra(select={'calorie': 'CAST(calorie AS INTEGER)'}).order_by('-calorie')
    return render(request, 'blog/post_calorie_high.html',{'posts': posts})

def post_protein_low(request):
    posts = Post.objects.extra(select={'protein': 'CAST(protein AS INTEGER)'}).order_by('protein')
    return render(request, 'blog/post_protein_low.html',{'posts': posts})

def post_protein_high(request):
    posts = Post.objects.extra(select={'protein': 'CAST(protein AS INTEGER)'}).order_by('-protein')
    return render(request, 'blog/post_protein_high.html',{'posts': posts})

def post_carbohydrate_low(request):
    posts = Post.objects.extra(select={'carbohydrate': 'CAST(carbohydrate AS INTEGER)'}).order_by('carbohydrate')
    return render(request, 'blog/post_carbohydrate_low.html',{'posts': posts})

def post_carbohydrate_high(request):
    posts = Post.objects.extra(select={'carbohydrate': 'CAST(carbohydrate AS INTEGER)'}).order_by('-carbohydrate')
    return render(request, 'blog/post_carbohydrate_high.html',{'posts': posts})
    
def post_lipid_low(request):
    posts = Post.objects.extra(select={'lipid': 'CAST(lipid AS INTEGER)'}).order_by('lipid')
    return render(request, 'blog/post_lipid_low.html',{'posts': posts})

def post_lipid_high(request):
    posts = Post.objects.extra(select={'lipid': 'CAST(lipid AS INTEGER)'}).order_by('-lipid')
    return render(request, 'blog/post_lipid_high.html',{'posts': posts})
