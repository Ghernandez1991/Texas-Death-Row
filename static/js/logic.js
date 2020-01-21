// GET is the default method, so we don't need to set it
fetch('/hello')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:');
        console.log(text); // Print the greeting as text
    });

// Send the same request
fetch('/hello')
    .then(function (response) {
        return response.json(); // But parse it as JSON this time
    })
    .then(function (json) {
        console.log('GET response as JSON:');
        console.log(json); // Here’s our JSON object
    })








// var defaulturl1 = `/scrape`;


// d3.json(defaulturl1, function(data) {
//   console.log(data);
// });








    // var selector1 = d3.select("#col-sm")
    
    
    
    // d3.json(defaulturl1).then(function (response){
    //     var words = [];
    //     var word_counts = [];
        
    //     for (i = 0; i < response.length; i++) {
    //       words.push(response[i].Most_Spoke_Words);
    //       word_counts.push(response[i].Count_Of_Words);
          
    //     }
    
    
    
    
    
    
    // var trace2 = {
    //       labels: words,
    //       values: word_counts,
    //       type: 'pie',
    //     };
    //     var data2 = [trace2];
    //     var layout2 = {
    //       title: {
    //         text: "Most Common Words in Last Statement",
    //         font: {
    //           family: "Helvetica, sans-serif",
    //           size: 25,
    //           color: "#229954"
    //         }
    //       }
    
    //     }
    //     Plotly.newPlot("selector1", data2, layout2);
    //   });


 
 
 

    




