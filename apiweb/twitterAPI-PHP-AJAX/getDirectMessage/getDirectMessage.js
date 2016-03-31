
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

	if (localStorage.length()==0) { //peut y avoir un probleme, si localStorage.length()!=0 au premier lancement
		localStorage.setItem("calls",1)
	}
	var nbrOfCalls = localStorage.getItem("calls");

	var appToUse = "app0";
	
	if (nbrOfCalls < 16) {
		appToUse = "app0";
	else if (nbrOfCalls < 31) {
		appToUse = "app1";
	else if (nbrOfCalls < 46) {
		appToUse = "app2";
	else if (nbrOfCalls == 46) {
		appToUse = "app0";
		localStorage.setItem("calls",1);

	localStorage.setItem("calls", nbrOfCalls+1)

	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php',
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
