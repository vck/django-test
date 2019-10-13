# django-test

```
Task:

Build one endpoint where you return the standard deviation of all measures
PM2.5, PM10, SO2, NO2, CO, O3 separately for temperatures below 
20 degrees and above 20 degrees (i.e. 6 measures x two temperature categories).

```

# Setup

gunicorn -b localhost:9000 mytest.wsgi

# API

/api -> GET

output:

```
below: {
	"PM2.5": val, 
	"PM10" : val, 
	"SO2"  : val, 
	"NO2"  : val, 
	"CO"   : val, 
	"O3"   : val
},

above: {
	"PM2.5": val, 
	"PM10" : val, 
	"SO2"  : val, 
	"NO2"  : val, 
	"CO"   : val, 
	"O3"   : val
}
```