import requests
import os
import json

if True:
	os.environ["http_proxy"] = "127.0.0.1:8888"
	os.environ["https_proxy"] = "127.0.0.1:8888"

class tvmaze:
	
	def __init__(self):
		self.headers = {"Accept":"application/json","Content-Type": "application/json"}

	def api_search_shows(self,query="",tvrage=None,thetvdb=None,imdb=None):
	
		url = "http://api.tvmaze.com/search/shows"
		headers = self.headers
		params = {"q" : query}
		if tvrage:
			params = {"tvrage" : tvrage}
		elif thetvdb:
			params = {"thetvdb" : thetvdb}	
		elif imdb:
			params = {"imdb" : imdb} 	
		else:
			params = {"q" : query}	
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}

	def api_search_people(self,query=""):
	
		url = "http://api.tvmaze.com/search/people"
		headers = self.headers
		params = {"q" : query}
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}	

	def api_search_shows_by_id(self,id=""):
	
		url = "http://api.tvmaze.com/shows/"+str(id)
		headers = self.headers
		params = {"embed[]" : "cast", "embed[] " : "episodes"}
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}

	def api_search_shows_episodes_by_id(self,id=""):
	
		url = "http://api.tvmaze.com/shows/"+str(id)+"/episodes"
		headers = self.headers
		params = {"specials" : "1"}
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}	

	def api_search_seasons(self,id=""):
	
		url = "http://api.tvmaze.com/shows/"+str(id)+"/seasons"
		headers = self.headers
		params = None
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}	

	def api_search_cast(self,id=""):
	
		url = "http://api.tvmaze.com/shows/"+str(id)+"/cast"
		headers = self.headers
		params = None
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}	

	def api_search_images(self,id=""):
	
		url = " http://api.tvmaze.com/shows/"+str(id)+"/images"
		headers = self.headers
		params = None
		data = None	
		try:
			response = requests.get(url=url,headers=headers,params=params,data=data)
			data = {"data" : response.text , "code" : response }
			return data
		except Exception as e:
			return {"error":e}													

			