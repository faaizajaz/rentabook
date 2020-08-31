$(document).ready(function() {
	$(".download-button").click(function(event) {
		event.preventDefault();
		$(".loader-div").html("<span class='loading-text'>Download in progress. Please be patient, this could take up to 5 minutes</span><div class='loader'></div>");

		$.each($("input[name='search-result']:checked"), function(){
			//alert($(this).attr("book-id"));

			//Do ajax to download, convert, and email
			var downloadURL = $(this).attr("download-api");

			$.ajax({
				type: 'post',
				url: downloadURL,
				data: {
					'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
				},
				dataType: 'json',
				success: function(data) {
					//alert(data['Title']);
					$(".loader-div").html("<h1>Success! " + data['Title'] + " was downloaded");

				}
			})
		});
	});
});