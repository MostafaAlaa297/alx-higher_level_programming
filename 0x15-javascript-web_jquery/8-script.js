$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(result){
	$.each(result.results, function(i, field){
        	$("UL#list_movies").append(`<li>${field.title}</li>`);
	})
});
