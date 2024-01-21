from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils.timezone import now
from django.contrib import messages

# Create your views here.
def main(request):
    allPosts = Post.objects.order_by('-timestamp')

    params = {"posts":allPosts}
    return render(request, 'blog/blogHome.html', params)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    allComments = Comment.objects.filter(post_id=post.id)
    post.views = post.views + 1
    post.save()

    if request.method == 'POST':
        comment = request.POST.get('comment')
        post_id = request.POST.get('post_id')
        parent = request.POST.get('comment_id')

        print(comment, post_id, parent)
        
        if parent == "":
            # Comment_id is None here
            myComment = Comment(user=request.user.username, content=comment, post_id=int(post_id))
            myComment.save()
            messages.add_message(request, messages.SUCCESS, "Your Comment has been posted succesfully!")

        else: 
            myComment = Comment(user=request.user.username, content=comment, post_id=int(post_id), comment_id=int(parent))
            myComment.save()
            messages.add_message(request, messages.SUCCESS, "Your reply has been posted succesfully!")

        return redirect(f"/blog/post/{post.slug}")
    
    replies= Comment.objects.filter(post_id=post.id).exclude(comment_id=None)
    # print([comment for comment in allComments if comment.comment_id==None])
    context = {"post":post, "comments":[comment for comment in allComments if comment.comment_id==None and comment.post_id == post.id], "replies":replies}

    return render(request, 'blog/blog.html', context)