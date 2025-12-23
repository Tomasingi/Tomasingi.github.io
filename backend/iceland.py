import json
import overpass
import osm2geojson

ICELAND_BBOX = '63,-25,68,-13'

def get_routes(api):
    bbox = ICELAND_BBOX
    query = ''.join([
        f'(',
        f'relation["type"="route"]["route"="road"]({bbox});',
        f');',
    ])
    result = api.get(query, verbosity='geom')

    path = '../scripts/routes_iceland_json.js'
    with open(path, 'w') as f:
        # geojson = osm2geojson.json2geojson(result.toJSON())
        f.write('var data = ')
        json.dump(result, f, indent=4)

def get_highways(api):
    bbox = ICELAND_BBOX
    query = ''.join([
        f'(',
        f'way["highway"="trunk"]({bbox});',
        f'way["highway"="trunk_link"]({bbox});',
        f'way["highway"="primary"]({bbox});',
        f'way["highway"="primary_link"]({bbox});',
        f'way["highway"="secondary"]({bbox});',
        f'way["highway"="secondary_link"]({bbox});',
        f');',
    ])
    result = api.get(query, verbosity='geom')

    path = '../scripts/highways_iceland_json.js'
    with open(path, 'w') as f:
        # geojson = osm2geojson.json2geojson(result)
        f.write('var data = ')
        json.dump(result, f, indent=4)

def main():
    api = overpass.API()

    get_highways(api)

if __name__ == '__main__':
    main()
