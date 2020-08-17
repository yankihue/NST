from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question, Comment, Post
from django.views import generic
from django.template.defaultfilters import slugify
from .forms import PostForm,CommentForm
from taggit.models import Tag


def home_view(request):
    posts = Post.objects.order_by('-published')
    
    # Show most common tags
    common_tags = Post.tags.most_common()[:25]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'posts': posts,
        'common_tags': common_tags,
        'form': form,
        
    }
    return render(request, 'polls/home.html', context)


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,

    }
    return render(request, 'polls/detail.html', context)

def post_detail(request, slug):
    template_name = 'polls/detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

                                           
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:25]

    # Filter posts by tag name
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
        'common_tags': common_tags,

        
    }
    return render(request, 'polls/home.html', context)

def submit(request):
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'form': form,   
    }
    return render(request, 'polls/submit.html', context)
