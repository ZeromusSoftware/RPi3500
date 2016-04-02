
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
		localStorage.setItem("calls",1);
	}
	var nbrOfCalls = localStorage.getItem("calls");

	localStorage.setItem("calls", nbrOfCalls+1);

	var i = nbrOfCalls.toString();
	
	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php',
		type: 'GET',
		data:'info='+i,
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
