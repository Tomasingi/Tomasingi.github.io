import json
from OSMPythonTools.overpass import Overpass
import osm2geojson

def main():
    bbox = '63,-25,68,-13'
    query = ''.join([
        f'relation["type"="route"]["route"="bus"]({bbox});',
        f'out geom;'
    ])
    overpass = Overpass()
    result = overpass.query(query)

    path = '../scripts/output.js'
    with open(path, 'w') as f:
        geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(geojson, f, indent=4)

if __name__ == '__main__':
    main()