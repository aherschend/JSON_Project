import json
from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

infile = open('US_fires_9_14.json')

firedata = json.load(infile)

lats, lons, bright = [],[],[]

for fire in firedata:
    if fire['brightness'] > 450:
        lat = fire['latitude']
        lon = fire['longitude']
        brightness = fire['brightness']
        lats.append(lat)
        lons.append(lon)
        bright.append(brightness)

print(lats[:5])
print(lons[:5])
print(bright[:5])

data = [{
     'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker' :{
        'size': 15,
        'color': bright,
        'colorscale': 'Rainbow',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }

}]

my_layout = Layout(title = "US Fires 9/14/2020 through 9/20/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename ='usfiredataendofSept2020.html')