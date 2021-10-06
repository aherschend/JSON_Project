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

# a quicker way to create the empty lists:
mags, lats, lons, hover_texts = [], [], [], []

#eq is a dictionary, list of eq's is a list so each element of it is a dictionary
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    mags.append(mag)
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]
    title = eq['properties']['title']
    lats.append(lats)
    lons.append(lons)
    hover_texts.append(title)


# to create a list [0:5] saying you want the first 5 elements
print(mags[:5])
print(lats[:5])
print(lons[:5])




data = [Scattergeo(lon=lons,lat=lats)]

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*m for m in mags], # that will increase by a factor of 5
        'color': mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title': 'Magnitude'}
    }
}]

my_layout = Layout(title="Global Earthquakes 30 Day")

fig = {'data':data,'layout':my_layout}


#This will great a file in our project so we can view it offline
offline.plot(fig,filename='globalearthquakes30day.html')