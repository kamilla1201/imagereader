import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from feed.models import Source, Image
#from feed.views import viewurl
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from lxml import etree
import urllib2
import urlparse
from django.core.urlresolvers import reverse
import urllib
from PIL import ImageFile
# Create your views here.
def home(request):
	return HttpResponseRedirect("/imagereader/feed/?url=all")

def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/imagereader/login/")
	sources = Source.objects.filter(user=request.user)
	return render(request, 'registration/profile.html', {'sources': sources})

def redirect_account(request):
	return HttpResponseRedirect("/imagereader/feed/?url=all")
def add_url(request):
	url = urlparse.unquote(request.POST['url'])
	min_width=int(request.POST['min_width'])
	min_height=int(request.POST['min_height'])
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
	if (len(Source.objects.filter(link = url, user = request.user)) == 0):
		source = Source(user = request.user, link = url, min_width=min_width, min_height=min_height)
		source.save()
		add_images(source)
	return HttpResponseRedirect("/imagereader/profile/")

def delete_url(request):
	link=request.POST['link']
	Source.objects.filter(link = link, user = request.user).delete()
	Image.objects.filter(source = link, user = request.user).delete()
	return HttpResponseRedirect("/imagereader/profile/")

def delete_images(request):
	link=request.POST['link']
	Image.objects.filter(source = link, user = request.user).delete()
	return HttpResponseRedirect("/imagereader/profile/")

def error(request):
	return render(request, 'error.html')

def add_images(source):
	url=source.link
	min_width = source.min_width
	min_height = source.min_height
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
	links = re.findall(r'https?://[^\s<>"]+(?:jpg|jpeg|bmp|png|gif)', page)
	for link in links:
		width, height = getsize(link)
		if width is None or height is None or cmp_size(min_width, width) or cmp_size(min_height, height):
			continue
		image = Image(user = source.user, source=url, link = link, width=width, height=height)
		image.save()

def update_filter(request):
	link=request.POST['link']
	min_width=int(request.POST['img_width'])
	min_height=int(request.POST['img_height'])
	filter_all=request.POST['filter_all']
	source = Source.objects.filter(link = link, user = request.user).update(min_width=min_width, min_height=min_height)
	
	if (filter_all == 'true'):
		if min_height > 0:
			images = Image.objects.filter(source = link, user = request.user, height__lt=min_height).delete()
		if min_width > 0:
			images = Image.objects.filter(source = link, user = request.user, width__lt=min_width).delete()

	return HttpResponseRedirect("/imagereader/profile/")


def cmp_size(min_value, actual_value):
	if min_value == 0 or min_value <= actual_value:
		return False
	return True

def getsize(uri):
    # get file size *and* image size (None if not known)
    file = urllib.urlopen(uri)
    p = ImageFile.Parser()
    width = None
    height = None
    while 1:
        data = file.read(25)
        if not data:
            break
        p.feed(data)
        if p.image:
            width, height = p.image.size
            break
    file.close()
    return width, height
