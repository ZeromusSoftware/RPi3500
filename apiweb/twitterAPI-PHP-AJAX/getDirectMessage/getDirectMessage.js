
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
	
	
	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php',
		type: 'GET',
		data:'info='+ appToUse,
		success: function(data) {
			/*
			var dataToUse = data.split("</br></br>")
			if (!localStorage.getItem("register0")) {
				for ( var i = 0; i < dataToUse.length; i++ ) {
					localStorage.setItem("register"+i.toString(),dataToUse[i]); //we can store only strings with localStorage
				}
			} else {
				for ( var i = 0; i < dataToUse.length; i++ ) {
					var index = dataToUse.indexOf(localStorage.getItem("register"+i.toString()));
					localStorage.setItem("register"+i.toString(),dataToUse[i]);
					if (index > -1) {
						dataToUse.splice(index,1);
					}
			}
			
			
			
			var messagesToPrint = data.split("out :");
			var currentMessages = document.getElementById('text').innerHTML.toString().split("out :");
			for ( var i = 0; i < currentMessages.length; i++ ) {
				var index = messagesToPrint.indexOf("out :" + currentMessages[i]);
				if (index > -1) {
					messagesToPrint.splice(index,1);
				}
			}
			var final_text = "";
			for (var i = 0; i < messagesToPrint.length; i++) {
				final_text = final_text + "out :" + messagesToPrint[i] + "</br></br>";
			}*/

			if(document.getElementById("loading")) {
				$("#text").html(data);
			} else {
				var truc = document.getElementById('text').innerHTML.toString();
				$("#text").prepend(data + "</br>");
			}
		},
		error: function(data) {
			alert("Error ajax getMessage");
		}	
	});
}
