import json
from OSMPythonTools.overpass import Overpass
import osm2geojson

def get_bicycle_routes_reykjavik(overpass):
    bbox = '63,-25,68,-13'
    query = ''.join([
        f'relation["type"="route"]["route"="bicycle"]({bbox});',
        f'out geom;'
    ])
    result = overpass.query(query)

    path = '../scripts/bicycle_routes_reykjavik_json.js'
    with open(path, 'w') as f:
        geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(geojson, f, indent=4)

def get_buses_reykjavik(overpass):
    bbox = '63,-25,68,-13'
    query = ''.join([
        f'relation["type"="route"]["route"="bus"]({bbox});',
        f'out geom;'
    ])
    result = overpass.query(query)

    path = '../scripts/buses_reykjavik_json.js'
    with open(path, 'w') as f:
        geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(geojson, f, indent=4)

def get_sl(overpass):
    bbox = '58.85,17.09,59.94,18.8'
    query = ''.join([
        f'(',
        f'relation["type"="route"]["network"="SL"]["route"="train"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["route"="subway"]({bbox});',
        f'relation["type"="route"]["network"="Stockholms tunnelbana"]["route"="subway"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["route"="light_rail"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["route"="tram"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["planned:route"="train"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["planned:route"="subway"]({bbox});',
        f'relation["type"="route"]["network"="Stockholms tunnelbana"]["planned:route"="subway"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["planned:route"="light_rail"]({bbox});',
        f'relation["type"="route"]["network"="SL"]["planned:route"="tram"]({bbox});',
        f');',
        f'out geom;'
    ])
    result = overpass.query(query)

    path = '../scripts/sl_json.js'
    with open(path, 'w') as f:
        geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(geojson, f, indent=4)

def get_istanbul(overpass):
    bbox = '40.8,28.6,41.4,29.7'
    query = ''.join([
        f'(',
        f'way["railway"="rail"]({bbox});',
        f'way["railway"="light_rail"]({bbox});',
        f'way["railway"="subway"]({bbox});',
        f'way["railway"="tram"]({bbox});',
        f'way["railway"="construction"]({bbox});',
        f');',
        f'out geom;'
    ])
    result = overpass.query(query)

    path = '../scripts/istanbul_json.js'
    with open(path, 'w') as f:
        geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(geojson, f, indent=4)

def main():
    overpass = Overpass()

    get_bicycle_routes_reykjavik(overpass)
    get_buses_reykjavik(overpass)
    get_sl(overpass)
    get_istanbul(overpass)

if __name__ == '__main__':
    main()