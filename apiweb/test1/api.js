
/*------------------------------------------------------*/
/*--------------------- ALL AJAX QUERIES ---------------*/
/*------------------------------------------------------*/


var reloadTime = 10000;


function getMessage() {
	//alert("getMessage enable");
	$.ajax({
		url: "get_message.php",
		type: GET,
		success: function(data) {
			$("#text").html($data[0].text);
			//alert("Ajax getMessage enable");
		},
		error: function(data) {
			//alert("Error ajax getMessage");
		}
	});
	
}


function postMessage() {
	//alert("postMessage enable");
	var message = encodeURIComponent($("#message").val());
	if (message != "") {
		//alert("postMessage if test enable");
		$.ajax({
			type: POST,
			url: "post_message.php",
			data: "message="+message,
			success: function(msg) {
				$("#text").append(msg);
				$("#message").val("GG");
				$("#message").focus();
				//alert("Ajax postMessage enable");
			},
			error: function(msg) {
				//alert("Error ajax postMessage");
			}
		});
	}
}


$(document).ready(function() {
	if(document.getElementById("message")) {
		window.setInterval(getMessage, reloadTime);
		$("#text").html("<h2>Test1</h2>");
		$("#text").append("Test2");
		$("#message").val("Test3");
		$("#message").focus();
		$("#button").click(postMessage());
	}
});




