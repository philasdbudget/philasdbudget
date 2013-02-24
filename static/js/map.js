var map = L.map('map').setView([39.958175, -75.160217], 13);

L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Map data &copy; <a href="http://www.esri.com/">ESRI</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);

var school_points;

var school_points = $.getJSON("/api/schools",
	function(json) { school_points = json;});

function create_handler(ulcs) {
	return function () {
		school_summary(ulcs);
	};
};

$(window).load(function() {
	for (var i = 0; i < school_points.length; i++) {
	    var ulcs = school_points[i].ulcs;
	    var circle = L.circle([school_points[i].geom[1], 
	    	school_points[i].geom[0]], 50, {
	    	fillColor: 'red',
	    	fillOpacity: 0.5,
	    	id: school_points[i].ulcs,
	    })
	    .on('click', create_handler(ulcs))
	    .addTo(map);
	};
});



function school_summary (ulcs) {
	$.getJSON("/api/budget/" + ulcs + "/181", function(data) {
		var html_string;
		console.log(data.items)
		for (var i = 0; i < data.items.length; i++) {
			console.log(data.items[i])
			html_string += "<li>" + data.items[i].item + ":" + data.items[i].amount + "</li>";
		};
		div = '<div class="school_summary"><h1>' + ulcs + '</h1>' + '<ul>' + html_string + '</ul></div>'
		console.log(div)
		$(".school-summaries").append(div);
	});
};
