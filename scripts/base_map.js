const mapCenters = {
    default: {pos: [64.12, -21.85], zoom: 11},
    reykjavik: {pos: [64.12, -21.85], zoom: 11},
    stockholm: {pos: [59.32, 18.06], zoom: 10},
    istanbul: {pos: [41.01, 28.95], zoom: 10},
    goteborg: {pos: [57.70, 11.97], zoom: 10},
}

const loc = location.pathname.split('/').slice(-1)[0].split('.')[0];
const center = mapCenters[loc] || mapCenters.default;

var map = L.map('map', {
    zoomDelta: 1,
    wheelPxPerZoomLevel: 120
}).setView(center.pos, center.zoom);

// var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     maxZoom: 18,
//     minZoom: 6,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: 'pk.eyJ1IjoiZGFzc2NoZWl0IiwiYSI6ImNqa3IxeHZzMDBvYWgza3Q5OWM5MzUzcHUifQ.6xj-BznboqX4wPfbvnnEGA',
// }).addTo(map);

const mtLayer = L.maptilerLayer({
    apiKey: 'BiZawqqKjurSA7iSzwT4',
    style: L.MaptilerStyle.DATAVIZ.LIGHT,
}).addTo(map);