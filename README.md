# django-test

```
Task:

Build one endpoint where you return the standard deviation of all measures
PM2.5, PM10, SO2, NO2, CO, O3 separately for temperatures below 
20 degrees and above 20 degrees (i.e. 6 measures x two temperature categories).

```

# Setup

- clone `git clone https://github.com/vck/django-test && cd django-test`

- build docker image `docker build -t django-test .`

- run server `docker run -p 8000:8000 django-test`

# API

- `/api/` -> GET

- curl `localhost:8000/api/`	

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

# notes

for CO that bellow 20 degree, the NaN value shows that there's no data, so the standard deviation becomes NaN.

```
import pandas as pd

df = pd.read_csv("staticfiles/data.csv")
print(df[df["CO"] < 20]["CO"])
```

when the above code executed, the output:

```
Series([], Name: CO, dtype: float64)
```

it shows that, for column CO, there's no data bellow 20 degrees, so when the output from
pandas converted to numpy array, the numpy array will also empty, thus results NaN standard deviation.