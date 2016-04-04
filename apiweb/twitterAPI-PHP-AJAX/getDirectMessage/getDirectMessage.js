
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
			
			var new_id = data.split(' - and last_id : ')[data.split(' - and last_id : ').length -1];
			if (new_id.length > 1) {
				localStorage.setItem("last_id",new_id);
			}
			var data_to_print = data.split(' - and last_id : ')[0];

			
			if(document.getElementById("loading")) {
				$("#text").html("<div class='get'>" + data_to_print + "</div>");
			} else {
				$("#text").prepend("<div class='get'>" + data_to_print + "</div>");
			}		
		},
		error: function(data) {
			alert("Error ajax getMessage");
		}	
	});
}
