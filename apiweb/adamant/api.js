
/*------------------------------------------------------*/
/*--------------------- ALL AJAX QUERIES ---------------*/
/*------------------------------------------------------*/


var reloadTime = 60000;


function getMessage() {
	$.ajax({
		url: 'test/get_message.php',
		type: 'GET',
		success: function(data) {
			if(document.getElementById("loading")) {
				$("#text").html(data);
			} else {
				$("#text").html(data);
			}
		},
		error: function(data) {
			alert("Error ajax getMessage");
		}
	});
}


function postMessage() {
	var message = encodeURIComponent($("#message").val());
	if (message != "") {
		$.ajax({
			type: 'POST',
			url: "test/post_message.php",
			data: "message="+message,
			success: function(msg) {
				$("#text").append($("#message").val());
				$("#message").val('');
				$("#message").focus();
				alert("Ajax postMessage enable");
			},
			error: function(msg) {
				alert("Error ajax postMessage");
			}
		});
	}
}


$(document).ready(function() {
	if(document.getElementById("message")) {
		window.setInterval(getMessage, reloadTime);
		$("#message").focus();
		$("#button").click(postMessage());
	}
});




