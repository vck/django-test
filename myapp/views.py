from django.http import HttpResponse, HttpResponseRedirect
import json
import pandas as pd 
import sys

filename = sys.path[0] + "/myapp/data/data.csv"

def index_view(request):
	data 	= dict(data=list(range(1, 100)))
	return HttpResponse(json.dumps(data))

def endpoint(request):

	df 		= pd.read_csv(filename)

	targets	= ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
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