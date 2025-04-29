from ..models.post_model import Post


def create_post(title, excerpt, image, date, slug, content, author, tags):
    new_post = Post(
        title=title,
        excerpt=excerpt,
        image=image,
        date=date,
        slug=slug,
        content=content,
        author=author,
        tags=tags
    )

    new_post.save()


def get_all_posts():
    return Post.objects.all()


def get_post_by_id(id):
    return Post.objects.get(id=id)


def get_post_by_slug(slug):
    return Post.objects.get(slug=slug) # slug is unique field


def get_post_comments(post):
    return post.comments.all()


def get_post_tags(post):
    return post.tags.all()
        
