String.prototype.toTitleCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

function itemgetter(i) {
    return function(t) { return t[i]; };
}

function sortf(data, getit) {
    data.sort(function(d1,d2) {
        if (getit(d1) < getit(d2)) {
            return 1;
        } else {
            return -1;
        }
    });
}

var schoolsRequest = $.getJSON('/api/schools');
var totalsRequest = $.getJSON('/api/schools/totals/181');

$.when(schoolsRequest, totalsRequest).done(
    function (schoolsResp, dataResp) {
        var schools = schoolsResp[0];
        var ulcs2name = {};
        for(var i in schools) {
            var s = schools[i];
            ulcs2name[s['ulcs']] =
                (s['school_name'] || 'Unknown').toTitleCase();
        }

        var data = dataResp[0];

        var normf = itemgetter('total_norm');
        var totalf = itemgetter('total');

        var getit = normf;
        sortf(data, getit);

        var width = $("#chart").css("width");
        width = parseInt(width.substring(0, width.length-2));
        var barHeight = 25;
        var gap = 2;
        var height = (barHeight + 2*gap) * data.length;

        var chart = d3.select($("#chart")[0])
                .append('svg')
                .attr('class', 'chart')
                .attr('width', width + 20)
                .attr('height', height + 40)
                .append('g')
                .attr("transform", "translate(10, 20)");

        var totals = data.map(getit);

        var x, y;

        x = d3.scale.linear()
            .domain([0, totals[0]])
            .range([0, width]);

        y = d3.scale.ordinal()
            .domain(data.map(function(d) { return d.ulcs.ulcs; }))
            .rangeBands([0, height]);

        chart.selectAll("rect")
            .data(data)
            .enter().append("rect")
            .attr("x", 0)
            .attr("y", function(d) { return y(d.ulcs.ulcs) + gap; })
            .attr("width", function(d) { return x(d.total_norm); })
            .attr("height", barHeight);

        chart.selectAll("text")
            .data(data)
            .enter().append("text")
            .attr("x", 0)
            .attr("y", function(d){ return y(d.ulcs.ulcs) + y.rangeBand()/2; } )
            .attr("dx", 5)
            .attr("dy", ".36em")
            .text(function(d) {
                return ulcs2name[d.ulcs.ulcs] || 'Unknown';
            });

    });
    // var margin = {top: 20, right: 20, bottom: 30, left: 100},
    //     width = 960 - margin.left - margin.right,
    //     height = 500 - margin.top - margin.bottom;

    // var formatPercent = d3.format(".0%");
    // var formatN = function(n) { return n / 1000.0; }

    // var x = d3.scale.ordinal()
    //     .rangeRoundBands([0, width], .1);

    // var y = d3.scale.linear()
    //     .range([height, 0]);

    // var xAxis = d3.svg.axis()
    //     .scale(x)
    //     .orient("bottom");

    // var yAxis = d3.svg.axis()
    //     .scale(y)
    //     .orient("left")
    //     //.tickFormat(formatN);

    // var svg = d3.select("body").append("svg")
    //     .attr("width", width + margin.left + margin.right)
    //     .attr("height", height + margin.top + margin.bottom)
    //   .append("g")
    //     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // $.getJSON('/api/schools/totals/181', function (data) {
    //     data.sort(function(d1,d2) {
    //         if (d1.total_norm < d2.total_norm) {
    //             return 1;
    //         } else {
    //             return -1;
    //         }
    //     });


    //     data.splice(0, 3);
    //     var maxv = data[2].total_norm;
    //     x.domain(data.map(function(d) { return d.ulcs.ulcs; }));
    //     y.domain([0, d3.max(data, function(d) { return d.total_norm; })]);

    //     svg.append("g")
    //         .attr("class", "x axis")
    //         .attr("transform", "translate(0," + height + ")")
    //         .call(xAxis);

    //     svg.append("g")
    //         .attr("class", "y axis")
    //         .call(yAxis)
    //         .append("text")
    //         .attr("transform", "rotate(-90)")
    //         .attr("y", 6)
    //         .attr("dy", ".71em")
    //         .style("text-anchor", "end")
    //         .text("Dollars");

    //     svg.selectAll(".bar")
    //         .data(data)
    //         .enter().append("rect")
    //         .attr("class", "bar")
    //         .attr("x", function(d) { return x(d.ulcs.ulcs); })
    //         .attr("width", x.rangeBand())
    //         .attr("y", function(d) { return y(d.total_norm); })
    //         .attr("height", function(d) { return height - y(d.total_norm); })
    //         .attr("fill", function(d) {
    //             return "rgb(140, 190, 120)";
    //         });
    // });
