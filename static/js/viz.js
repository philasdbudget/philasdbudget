var margin = {top: 20, right: 20, bottom: 30, left: 100},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var formatPercent = d3.format(".0%");
var formatN = function(n) { return n / 1000.0; }

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    //.tickFormat(formatN);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

$.getJSON('/api/schools/totals/181', function (data) {
    data.sort(function(d1,d2) {
        if (d1.total_norm < d2.total_norm) {
            return 1;
        } else {
            return -1;
        }
    });

    var maxv = data[2].total_norm;

    x.domain(data.map(function(d) { return d.ulcs.ulcs; }));
    y.domain([0, d3.max(data, function(d) { return d.total_norm; })]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Dollars");

    svg.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.ulcs.ulcs); })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return y(d.total_norm); })
        .attr("height", function(d) { return height - y(d.total_norm); })
        .attr("fill", function(d) {
            return "rgb(70, 20, 60)";
        });
});
