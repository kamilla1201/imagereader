from django.shortcuts import render
from .models import Post, Source, Image
import urlparse
import urllib2
import re
from lxml import etree
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def list(request):
	all_images = []
	images = []
	links = []
	sources = []
	if request.user.is_authenticated():
		sources = Source.objects.filter(user=request.user)
		if request.GET.get('url'):
			link_list = request.GET.getlist('url')
			if 'all' in link_list:
				if len(link_list) > 1:
					return HttpResponseRedirect("/imagereader/feed/?url=all")
				links.append('all')
				link_list = [source.link for source in sources]
		else:
			return HttpResponseRedirect("/imagereader/feed/?url=all")
			#all_images = Image.objects.filter(user=request.user)
		for link_ in link_list:
			link = urlparse.unquote(link_)
			all_images.extend(Image.objects.filter(user=request.user, source=link))
			links.append(link)
		all_images.sort(key=lambda x: x.id, reverse=True)
		paginator = Paginator(all_images, 10) # Show 25 images per page
		page = request.GET.get('page')
		try:
			images = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			images = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			images = paginator.page(paginator.num_pages)

	#return render_to_response('feed/list.html', {'images': images})
	return render(request, 'feed/list.html', {'images': images, 'links': links, 'sources': sources})

def viewurl(request, images):
	return render(request, 'feed/list.html', {'images': images})


def submit(request):
	url=request.POST['url']
	val = URLValidator()
	try:
		val(url)
	except:
		return HttpResponseRedirect("/imagereader/error/")
	req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0'})
	page = urllib2.urlopen(req).read()
	try:
		tree = etree.XML(page)
	except:
		return HttpResponseRedirect("/imagereader/error/")
	items = tree.xpath('/rss/channel/item')
	posts = []
	for item in items:
		if ( item.find('enclosure') == None):
				continue
		title = item.find('title').text
		date = datetime.strptime(item.find('pubDate').text[:-6], '%a, %d %b %Y %H:%M:%S')
		link = item.find('link').text
		image = item.find('enclosure').get('url')
		post = Post(date = date, title = title, link = link, image = image)
		posts.append(post)
	return render(request, 'feed/list.html', {'posts': posts})
	#url = reverse('/imagereader/feed/', kwargs={'posts': posts})
	#return HttpResponseRedirect(url)


