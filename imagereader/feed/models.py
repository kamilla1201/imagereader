from django.db import models
from composite_field import CompositeField
# Create your models here.
class Post(models.Model):
	date = models.DateTimeField('Date', auto_now_add=True)
	title = models.CharField('Title', max_length = 100)
	link = 	models.URLField('Link')	
	image = models.URLField('Image')	
	class Meta:
		verbose_name = 'article'
		verbose_name_plural = 'articles'

	def __str__(self):
		return self.title


class Source(models.Model):
    user = models.ForeignKey('auth.User')
    link = models.URLField('Link')
    min_width = models.PositiveSmallIntegerField(default=0)
    min_height = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.user.username + ':' + self.link

class Image(models.Model):
    user = models.ForeignKey('auth.User')
    source = models.URLField('Source')
    link = models.URLField('Link')
    width = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.user.username + ':' + self.link