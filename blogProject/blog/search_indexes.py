from haystack import indexes
from .models import Post

"""
create indexes for the contents in Post
'document=True' indicates the search engine will retrieve based on 'text' field
 'use_template=True' indicates we can use template to build the index file
"""

class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
