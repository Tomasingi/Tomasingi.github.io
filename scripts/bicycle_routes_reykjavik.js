function style(feature) {
    st = {
        weight: 1,
        opacity: 1,
        color: '#000',
        dashArray: '',
        fillOpacity: 0.7,
    };

    if (feature.properties.tags.network === 'rcn') {
        st.weight = 5;
    } else if (feature.properties.tags.network === 'lcn') {
        st.weight = 3;
        st.color = '#888';
    }

    if (feature.properties.tags.colour) {
        st.color = feature.properties.tags.colour;
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
    stringArray.push('<p>' + props.tags.name + '</p>');

    this._div.innerHTML = stringArray.join('');
};

info.move = function (e) {
    const mapWidth = document.getElementById('map').offsetWidth;
    const linksWidth = document.getElementById('links').offsetWidth;
    const offsetX = this._div.offsetWidth;
    const baseOffsetY = document.getElementById('map').offsetTop;
    const offsetY = this._div.offsetHeight;
    this._div.style.left = e.pageX - linksWidth - mapWidth - 0.5*offsetX + 'px';
    this._div.style.top = e.pageY - baseOffsetY - offsetY + 'px';
}

document.addEventListener('mousemove', function (e) {
    info.move(e);
});

info.addTo(map);

function highlightFeature(e) {
    var layer = e.target;

    if (layer.feature.properties.tags.network === 'rcn') {
        layer.setStyle({
            weight: 10
        });
    }

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
        click: zoomToFeature,
    });
}

geojson = L.geoJson(data, {
    style: style,
    onEachFeature: onEachFeature,
}).addTo(map);