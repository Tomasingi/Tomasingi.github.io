import json

def main():
    input_path = 'vagnar.json'
    output_path = '../scripts/bus_colors.js'

    with open(input_path, 'r') as f:
        data = json.load(f)

    bus_colors = {}
    for route in data['leidir']:
        path = route['ferlar'][0]
        number = path['ferill'].split('-')[0]
        color = path['komur'][0]['col']

        bus_colors[number] = color

    with open(output_path, 'w') as f:
        f.write('var bus_colors = ')
        json.dump(bus_colors, f, indent=4)

if __name__ == '__main__':
    main()