from expressPr.celery import app
from blog.models import Post


@app.task
def set_is_deleted_true_task(post_ids):
    posts = Post.objects.filter(id__in=post_ids)
    for post in posts:
        post.is_deleted = True
        post.save()
