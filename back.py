from flask import Flask, render_template
import googlemaps

app = Flask(__name__)

@app.route("/maps")
def map():
    return render_template("maps.html")
@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

if (__name__ == "__main__"):
    app.run(debug=True)

API_KEY = "AIzaSyA5X4xrlmTvcqbFPUYC2DJTxLK49Xv6vZQ"

gmaps = googlemaps.Client(key = API_KEY)

a = input ("Enter address\n")
geocode_result = gmaps.geocode(a)
try:
    lat = geocode_result[0]["geometry"]['location']['lat']
    long = geocode_result[0]["geometry"]['location']['lng']
except:
    lat = None
    lng = None

places_result = gmaps.places_nearby(location="{},{}".format(lat,long) , radius = 2000, open_now = False, type = 'convenience_store')

#pprint.pprint(places_result)

locations=[]
for i in places_result["results"]:
    if (i["name"] == "7-Eleven"):
        locations.append(i)
    else:
        continue

for i in locations:
    print(i,"\n")
