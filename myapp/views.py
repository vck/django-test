from django.http import HttpResponse
import json
import pandas as pd 
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
FILENAME = ROOT_DIR+"/staticfiles/data.csv"

def index_view(request):
	data = dict(msg="Hello!", plain="Antler", md5="fc4acdfe839b3b71bbc4d702ff3220")
	return HttpResponse(json.dumps(data))

def endpoint(request):
	df 		= pd.read_csv(FILENAME)
	targets	= ["PM2.5", 
				"PM10", 
				"SO2", 
               	"NO2", 
               	"CO",
               	"O3"]

	data 	= dict()
	bellow	= dict()
	above	= dict()

	for target in targets:
		bellow[target]	= df[df[target] < 20][target].to_numpy().std()
		above[target]	= df[df[target] > 20][target].to_numpy().std()
	
	data["bellow"]	= bellow
	data["above"]	= above
	return HttpResponse(json.dumps(data))