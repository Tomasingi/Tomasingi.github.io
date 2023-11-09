var map = L.map('map').setView([64.12, -21.85], 11);

var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    minZoom: 6,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZGFzc2NoZWl0IiwiYSI6ImNqa3IxeHZzMDBvYWgza3Q5OWM5MzUzcHUifQ.6xj-BznboqX4wPfbvnnEGA'
}).addTo(map);

function style(feature) {
    st = {
        // fillColor: '#ff7800',
        weight: 6,
        opacity: 1,
        color: '#000',
        dashArray: '',
        fillOpacity: 0.7
    };

    if (bus_colors[feature.properties.tags.ref]) {
        st.color = bus_colors[feature.properties.tags.ref];
    }

    return st;
}

var geojson;

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div');
    this._div.id = 'info';
    this.update();
    return this._div;
};

info.update = function (props) {
    if (!props) {
        this._div.style.display = 'none';
        return;
    }

    this._div.style.display = 'inherit';
    const stringArray = [];
    stringArray.push('<p><b>Leið ' + props.tags.ref
        + ': </b>' + props.tags.from
        + ' - ' + props.tags.to
        + '</p>');
    if (props.tags.via) {
        stringArray.push('<p>Via: ' + props.tags.via.split(';').join(', ') + '</p>');
    }

    this._div.innerHTML = stringArray.join('');
};

info.move = function (e) {
    const mapWidth = document.getElementById('map').offsetWidth;
    const offsetX = this._div.offsetWidth;
    const baseOffsetY = document.getElementById('map').offsetTop;
    const offsetY = this._div.offsetHeight;
    this._div.style.left = e.pageX - mapWidth - 0.5*offsetX + 'px';
    this._div.style.top = e.pageY - baseOffsetY - offsetY + 'px';
}

document.addEventListener('mousemove', function (e) {
    info.move(e);
});

info.addTo(map);

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 12
    });

    info.update(layer.feature.properties);

    layer.bringToFront();
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

geojson = L.geoJson(data, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);