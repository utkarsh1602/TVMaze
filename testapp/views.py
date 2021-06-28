from django.shortcuts import render
from util.tvmaze import tvmaze
import json
import random
from bs4 import BeautifulSoup

# Create your views here.
def get_shows(request):

	tv = tvmaze()
	data = tv.api_search_images(id=str(random.randint(10,600)))
	images_list = list()
	for item in json.loads(data.get("data")):
		images_list.append(item.get("resolutions").get("original").get("url"))
	return render(request,"index.html",{"data":images_list})

def single_view(request):	
	id = "100"

	if request.method=="GET":
		if request.GET.get('id'):
			id = request.GET['id']

	tv = tvmaze()
	item = tv.api_search_shows_by_id(id=id)
	item = json.loads(item.get("data"))
	temp = {}

	temp['id']=item.get("id") or None
	temp['image']=item.get("image").get("original") or None
	temp['name']=item.get("name") or None
	# temp['genres']=",".join(item.get("genres")) if type(item.get("show").get("genres"))==list else item.get("show").get("genres")
	# temp['language']=item.get("language")
	# temp['type']=item.get("type")
	# temp['network']=item.get("network").get("name")
	# temp['rating']=item.get("rating").get("average")
	
	soup = BeautifulSoup(item.get("summary"), 'html.parser')
	temp['summary']=soup.get_text()
	
	a=list()
	for cast in item.get("_embedded").get("cast"):
		try:
			a.append(cast.get("person",{}).get("image",{}).get("original") or {})
		except:
			pass	
	temp['cast']=a	

	return render(request,"single.html",{"data":temp})

def search(request):	
	query = "India"

	if request.method=="GET":
		if request.GET.get('search'):
			query = request.GET['search']

	tv = tvmaze()
	data = tv.api_search_shows(query=query)

	shows_list = list()
	for item in json.loads(data.get("data")):
		temp = {}
		try:
			temp['id']=item.get("show").get("id")
			temp['image']=item.get("show").get("image").get("original")
			temp['name']=item.get("show").get("name")
			temp['genres']=",".join(item.get("show").get("genres")) if type(item.get("show").get("genres"))==list else item.get("show").get("genres")
			temp['language']=item.get("show").get("language")
			temp['type']=item.get("show").get("type")
			temp['network']=item.get("show").get("network").get("name")
			temp['rating']=item.get("show").get("rating").get("average")
			soup = BeautifulSoup(item.get("show").get("summary"), 'html.parser')
			temp['summary']=soup.get_text()
			if temp.get("summary"):
				shows_list.append(temp)
		except:
			pass	

	return render(request,"list_view.html",{"data":shows_list})	
