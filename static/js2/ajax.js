$(function(){
	$('#insOf').click(function(){
		$.ajax({
			type: "POST",
			url: "/mostrarOfertas/",
			data: {
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	
	
	});
});	

function searchSuccess(data, textStatus, jqXHR){
	$('#showOf').html(data);
}
