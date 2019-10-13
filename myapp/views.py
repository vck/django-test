from django.http import HttpResponse
import json
import pandas as pd 
import sys

FILENAME = sys.path[0] + "/myapp/data/data.csv"

def index_view(request):
	data = "hello world!"
	return HttpResponse(json.dumps(data))

def endpoint(request):
	df 		= pd.read_csv(FILENAME)
	targets	= ["PM2.5", 
				"PM10", 
				"SO2", 
				"NO2", 
				"CO", 
				"O3"]
	data = dict()
	bellow = dict()

	for target in targets:
		bellow[target] = df[df[target] < 20][target].to_numpy().std()
	data["bellow"] = bellow
	
	above = dict()
	for target in targets:
		above[target] = df[df[target] > 20][target].to_numpy().std()
	data["above"] = above
	return HttpResponse(json.dumps(data))