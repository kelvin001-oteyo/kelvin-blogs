
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Category
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

from .form import CommentForm
from django.shortcuts import render



from .models import Post, Category

def home(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories
    })




def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
        'comments': comments
    })

  
  

 

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')



def posts_by_category(request, category_name):
    posts = Post.objects.filter(category__name=category_name)
    return render(request, 'blog/home.html', {'posts': posts})
