









d3.json("/json").then(function (data) {
    console.log(data)
});




function buildpie() {

    var selector1 = d3.select("#col-sm1")



    d3.json("/json").then(function (response) {
        var words = response.Most_Spoken_Words;
        var word_counts = response.Count_of_Words;

       
        var data = [{
            values: word_counts,
            labels: words,
            textinfo: "label+percent",
            textposition: "inside",
            type: 'pie'
        }];

        var layout = {
            height: 1000,
            width: 1600
        };

        var graph = document.getElementById('graph');
        Plotly.newPlot(graph, data, layout);


    })



    
    
    










    


};

buildpie();