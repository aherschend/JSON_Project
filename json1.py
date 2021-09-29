import json

infile = open('eq_data_1_day_m1.json', 'r')
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
    lat = eq['geometry']['coordinates'][0]
    lon = eq['geometry']['coordinates'][1]
    lats.append(lat)
    lons.append(lon)

print(mags)
print(lats)
print(lons)


