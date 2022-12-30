from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group
from .forms import PostForm

POST_LIMIT: int = 10


def authorized_only(func):
    """Check authorisation of User"""
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')
    return check_user


def owner_only(func):
    """Check post owner"""
    def check_owner(request, post_id, *args, **kwargs):
        author = request.user
        post = author.posts.filter(id__exact=post_id)
        if post:
            return func(request, post_id, *args, **kwargs)
        return redirect(f'/posts/{post_id}/')
    return check_owner


def index(request):
    """Main page"""

    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts_list = Post.objects.select_related('author', 'group').all()
    paginator = Paginator(posts_list, POST_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_post(request, slug):
    """Page of group"""

    group = get_object_or_404(Group, slug=slug)
    posts_list = group.posts.all()
    paginator = Paginator(posts_list, POST_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'posts/group_list.html'
    title = f'Записи сообщества {group.title}'

    context = {
        'title': title,
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    """Page of user profile"""
    User = get_user_model()

    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    post_count = posts.count()
    paginator = Paginator(posts, POST_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'post_count': post_count,
        'author': author,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    """Page of post detail"""

    post = get_object_or_404(Post, id=post_id)
    post_count = Post.objects.select_related('author', 'group').filter(
        author__exact=post.author).count()

    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


@authorized_only
def post_create(request):
    """Page for create new post"""

    title = 'Новый пост'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            new = Post.objects.create(
                author=user,
                text=form.cleaned_data['text'],
                group=form.cleaned_data['group'],
            )
            new.save()
            return redirect(f'/profile/{user.username}/')
        return render(request, 'posts/create_post.html', {
            'form': form,
            'title': title
        })

    form = PostForm()
    return render(request, 'posts/create_post.html', {
        'form': form,
        'title': title
    })


@owner_only
def post_edit(request, post_id):
    """Page of edit post"""

    title = 'Редактировать пост'
    is_edit = True

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=post_id)
            post.text = form.cleaned_data['text']
            post.group = form.cleaned_data['group']
            post.save()
            return redirect(f'/posts/{post_id}/')
        return render(request, 'posts/create_post.html', {
            'form': form,
            'title': title,
            'is_edit': is_edit,
        })

    post = Post.objects.get(id=post_id)
    form = PostForm()
    form.fields['text'].initial = post.text
    form.fields['group'].initial = post.group

    return render(request, 'posts/create_post.html', {
        'form': form,
        'title': title,
        'is_edit': is_edit,
    })
