import requests as rq
import json
import goslate

gs= goslate.Goslate()

def chucknorris(mot):
	payload={'query':mot}
	r = rq.get('https://api.chucknorris.io/jokes/search', params=payload).json()
	r=r["result"][0]["value"]
	fr=gs.translate(r,'fr')
	return fr

chucknorris('hello')
