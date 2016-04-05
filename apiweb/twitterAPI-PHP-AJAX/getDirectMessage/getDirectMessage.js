
/*********************************************************
 * Feature to get last direct messages
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/
 
/* Update the URL to go to getDirectMessage.php */
function getDirectMessage() { 

	if (!localStorage.getItem("calls")) {
		localStorage.setItem("calls","1"); //we can store only strings with localStorage
	}
	var nbrOfCalls = +localStorage.getItem("calls"); // "+" converts string to integer

	localStorage.setItem("calls", (nbrOfCalls+1).toString());

	var appToUse = (nbrOfCalls%3).toString();

	if (!localStorage.getItem("last_id") || localStorage.getItem("last_id")=="0") {
		localStorage.setItem("last_id","717044642315968515");
	}
	var last_id_printed = localStorage.getItem("last_id");
	
	
	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php',
		type: 'GET',
		data:'info='+ appToUse + "&last_id=" + last_id_printed,
		success: function(data) {


			var d = new Date();
			var h = d.getHours();
			var m = d.getMinutes();
			var s = d.getSeconds();
			var day = d.getDate();
			var M = +d.getMonth()+1;
			var Y = d.getFullYear();

			var message_caracteristics = day + "/" + M + "/" + Y + " - " + h + ":" + m + ":" + s + " - RPi --> ";

			
			var new_id = data.split(' - and last_id : ')[data.split(' - and last_id : ').length -1];

			if (new_id.length > 1) {
				localStorage.setItem("last_id",new_id);
			}

			var data_to_print = data.split(' - and last_id : ')[0];

			var shell_output = data_to_print.split("---splitstring---")[0];

			var gpio_pins_status = "000000000";

			if (data_to_print.split("---splitstring---").length == 2) {
				gpio_pins_status = data_to_print.split("---splitstring---")[0];
			}

			$("#temperature").html(gpio_pins_status);
			
			if(document.getElementById("loading")) {
				if (shell_output.length > 0) {
					$("#text").html("<div class='get'>" + shell_output + "</div>");
				}else {
					$("#text").html("<div class='get'>enter a command..</div>");
				}
			} else {
				if (shell_output.length > 1) {
					$("#text").append("<div class='get'>" + shell_output + "</div>");
				}
			}
		},
		error: function(data) {
			alert("Error ajax getMessage");
		}	
	});
}
