from django.contrib.syndication.views import Feed
from .models import Post


class RssFeed(Feed):
    title="Yilin's Blog"
    link="/"
    description="Thanks for your subscription."

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}] {}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body