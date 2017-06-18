from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment
from blog.models import Post
from .form import CommentForm

# Create your views here.


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)

    # post a new comment
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            # if data is invalid, re-render the detail page
            # get all the comments given then specific post
            #
            # contains original comment form with POST contents,
            # and show the invalid errors
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context)

    # post no comments
    #
    # redirect() method accept the 'post' model instance as argument,
    # and call the model's get_absolute_url() method in Post class in 'blog/models.py'.
    # After that, it reverse-resolve the view name('blog:detail') and sends to views.detail to handle
    #
    # contains new comment form
    return redirect(post)

