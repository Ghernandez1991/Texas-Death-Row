d3.json('/json').then(function(data) {
	console.log(data);
});

function buildpie() {
	var selector1 = d3.select('#col-sm1');

	d3.json('/json').then(function(response) {
		var words = response.Most_Spoken_Words;
		var word_counts = response.Count_of_Words;

		var data = [
			{
				values: word_counts,
				labels: words,
				textinfo: 'label+percent',
				textposition: 'inside',
				type: 'pie'
			}
		];

		var layout = {
			height: 800,
			width: 725,
			plot_bgcolor: 'black',
			paper_bgcolor: '#FFF3',
			title: {
				text: 'Most Common Final Words',

				font: {
					family: 'Courier New, monospace',
					size: 24,
					color: '#d10200'
				},
				xref: 'paper',
				x: 0.05
			}
		};

		var graph = document.getElementById('graph');
		Plotly.newPlot(graph, data, layout, { scrollZoom: true });
	});
}

function buildpie2() {
	var selector1 = d3.select('.tester');

	d3.json('/top_ten').then(function(response) {
		var counties = [];
		var counts = [];
		for (i = 0; i < response.length; i++) {
			counties.push(response[i].Count);
			counts.push(response[i].County);
		}

		var data = [
			{
				values: counties,
				labels: counts,
				textinfo: 'label+percent',
				textposition: 'inside',
				type: 'pie'
			}
		];

		console.log(counties);
		console.log(counts);

		var layout = {
			height: 800,
			width: 725,
			plot_bgcolor: 'black',
			paper_bgcolor: '#FFF3',
			title: {
				text: 'Most Active County For Executions',
				font: {
					family: 'Courier New, monospace',
					size: 24,
					color: '#d10200'
				},
				xref: 'paper',
				x: 0.05
			}
		};

		var graph = document.getElementById('tester');
		Plotly.newPlot(graph, data, layout, { scrollZoom: true });
	});
}

buildpie();
buildpie2();
