import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json','w')

eqdata = json.load(infile) 

# to decide the number of indent, you just play around with it
json.dump(eqdata,outfile, indent=4)



print(len(eqdata["features"]))


list_of_eqs = eqdata["features"]

mags = []
lats = []
lons = []

#eq is a dictionary, list of eq's is a list so each element of it is a dictionary
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    mags.append(mag)
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]
    lats.append(lat)
    lons.append(lon)


# to create a list [0:5] saying you want the first 5 elements
print(mags[:5])
print(lats[:5])
print(lons[:5])


from plotly.graph_objs import Scattergeo, layout
from plotly import offline


data = [Scattergeo(lon=lons,lat=lats)]

my_layout = Layout(title="Global Earthquakes 30 Day")

fig = {'data':data,'layout':my_layout}


#This will great a file in our project so we can view it offline
offline.plot(fig,filename='globalearthquakes30day.html')