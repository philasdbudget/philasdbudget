var map = L.map('map').setView([39.958175, -75.160217], 13);

L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Map data &copy; <a href="http://www.esri.com/">ESRI</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);

var school_points;

var school_points = $.getJSON("/js/schools.json", function(json) { school_points = json;});

L.geoJson(school_points).addTo(map);
