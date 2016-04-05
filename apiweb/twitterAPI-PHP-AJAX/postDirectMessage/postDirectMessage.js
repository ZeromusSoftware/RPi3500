
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

	localStorage.setItem("pushes", (nbrOfPushes+1).toString());

	var appToUse = (nbrOfPushes%3).toString();
	
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
