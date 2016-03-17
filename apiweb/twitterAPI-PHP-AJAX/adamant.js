
/*********************************************************
 * Adamant API's main page
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/
 

var reloadTime = 60000;

$(document).ready(function() {
	if(document.getElementById("message")) {
		window.setInterval(getDirectMessage, reloadTime);
		$("#message").focus();
		$("#button").click(postDirectMessage());
	}
});
