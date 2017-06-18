from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
import markdown


class Category(models.Model):
    cate_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cate_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # simple way to calculate how many people read the post
    # ignore situation that multiple people read the same post the same time
    def increase_hits(self):
        self.hits += 1
        # save the updated number of views
        self.save(update_fields=['hits'])

    # rewrite sava() method for striping the post body as a excerpt automatically
    def save(self, *args, **kwargs):
        # if there is no excerpt
        if not self.excerpt:
            # create a Markdown instance for rendering post body
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])

            # render Markdown body as HTML
            # strip_tags() for striping HTML tag
            # take the first 50 characters as excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:50]

        super(Post,self).save(*args, **kwargs)







