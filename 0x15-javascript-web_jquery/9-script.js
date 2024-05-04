$.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(result){
	$("DIV#hello").text(Object.keys(result)[1]);
});
