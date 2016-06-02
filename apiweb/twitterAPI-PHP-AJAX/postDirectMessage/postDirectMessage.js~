
/*********************************************************
 * Feature to send a new direct message
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/
 
 
 /* Update the URL to go to getDirectMessage.php */
function postMessage() {


	if (!localStorage.getItem("pushes")) {
		localStorage.setItem("pushes","1"); //we can store only strings with localStorage
	}
	var nbrOfPushes = +localStorage.getItem("pushes"); // "+" converts string to integer

	if (nbrOfPushes>=7){
		localStorage.setItem("pushes","1");
		nbrOfPushes=1;
	} else {
		localStorage.setItem("pushes", (nbrOfPushes+1).toString());
	}
	var appToUse = nbrOfPushes.toString();
	
	var message = encodeURIComponent($("#message").val());

	if (message != "") {
		$.ajax({
			type: 'POST',
			url: "/twitterAPI-PHP-AJAX/postDirectMessage/postDirectMessage.php",
			data: "message="+message+"&info="+appToUse,
			success: function(msg) {
				
				var d = new Date();
				var h = d.getHours();
				var m = d.getMinutes();
				var s = d.getSeconds();
				var day = d.getDate();
				var M = +d.getMonth()+1;
				var Y = d.getFullYear();

				var message_caracteristics = day + "/" + M + "/" + Y + " - " + h + ":" + m + ":" + s + " - Adamant --> "; 
	
				if(document.getElementById("loading")) {
					$("#text").html("</br><div class='sent'>" + message_caracteristics + $("#message").val() + "</div>");
				} else {
					$("#text").append("</br><div class='sent'>" + message_caracteristics + $("#message").val() + "</div>");
				}
				$("#message").val('');
				$("#message").focus();
			},
			error: function(msg) {
				alert("Error ajax postMessage");
			}
		});
	}
}
/*
function turnOnOffComponent(var component_pin, var status_to_set) { //"status_to_set must be 0 or 1"

	

	if (!localStorage.getItem("pushes")) {
		localStorage.setItem("pushes","1"); //we can store only strings with localStorage
	}
	var nbrOfPushes = +localStorage.getItem("pushes"); // "+" converts string to integer

	if (nbrOfPushes>=7){
		localStorage.setItem("pushes","1");
		nbrOfPushes=1;
	} else {
		localStorage.setItem("pushes", (nbrOfPushes+1).toString());
	}
	var appToUse = nbrOfPushes.toString();

	var message = "";

	if ((status_to_set.toString() == "0" || status_to_set.toString() == "1") && component_pin.length == 2) {
		message = "*****{gpio_setting}:" + component_pin + status_to_set;
	}
	if (message.length > 0) {
        	$.ajax({
			type: 'POST',
			url: "/twitterAPI-PHP-AJAX/postDirectMessage/postDirectMessage.php",
			data: "message="+message+"&info="+appToUse,
			success: function(msg) {
				
				document.getElementById(id).style.background='lightgrey'; // Au click le bouton devient gris clair
				
				
			},
			error: function(msg) {
				alert("Error ajax postMessage");
			}
		});
	}

}*/
