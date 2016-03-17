
/*********************************************************
 * Feature to send a new direct message
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/
 
 
function postMessage() {
	var message = encodeURIComponent($("#message").val());
	if (message != "") {
		$.ajax({
			type: 'POST',
			url: "postDirectMessage/postDirectMessage.php",
			data: "message="+message,
			success: function(msg) {
				if(document.getElementById("text")) {
					$("#text").append($("#message").val());
				}
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
