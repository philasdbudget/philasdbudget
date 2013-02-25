var map = L.map('map').setView([39.958175, -75.160217], 13);

L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Map data &copy; <a href="http://www.esri.com/">ESRI</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
}).addTo(map);

var school_points = $.getJSON("/api/schools",
	function(json) { school_points = json;});

function create_handler(ulcs, name, address) {
	return function () {
		school_summary(ulcs, name, address);
	};
};

$(window).load(function() {
	$.getJSON("/api/schools",
		function(school_points) {
			console.log(school_points);
			for (var i = 0; i < school_points.length; i++) {
			    var ulcs = school_points[i].ulcs;
			    var name = school_points[i].school_name;
			    var address = school_points[i].address;
			    var circle = L.circle([school_points[i].geom[1], 
			    	school_points[i].geom[0]], 100, {
			    		stroke: false,
			    		color: '#03f',
			    		fillColor: '#03f',
			    		opacity: .5,
			    		fillOpacity: .5,
			    	})
			    	.on('click', create_handler(ulcs, name, address))
			    	.addTo(map);
			};
		});
});



function school_summary (ulcs, name, address) {
	var summary_count = $(".school_summary").length;
	if (summary_count == 3) {
		$('.school_summary').first().remove();
	}
	$.getJSON("/api/budget/" + ulcs + "/181", function(data) {
		var html_string = "";
		for (var i = 0; i < data.items.length; i++) {
			html_string += "<li>" + data.items[i].item + ": $" + data.items[i].amount + "</li>";
		};
		div = '<div class="school_summary span3"><h3>' + name + '</h3>' + '<h4>' + address + '</h4>' + '<ul>' + html_string + '</ul></div>'
		$(".school-summaries").append(div);
	});
};
