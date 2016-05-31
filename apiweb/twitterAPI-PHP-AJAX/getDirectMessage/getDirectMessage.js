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
	
	if (nbrOfCalls>=7){
		localStorage.setItem("calls","1");
		nbrOfCalls=1;
	} else {
		localStorage.setItem("calls", (nbrOfCalls+1).toString());
	}
	var appToUse = nbrOfCalls.toString();

	if (!localStorage.getItem("last_id") || localStorage.getItem("last_id")=="0") {
		localStorage.setItem("last_id","717044642315968515");
	}
	var last_id_printed = localStorage.getItem("last_id");
	
	
	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php',
		type: 'GET',
		data:'info='+ appToUse + "&last_id=" + last_id_printed,
		success: function(data) {

			
			var new_id = data.split(' - and last_id : ')[data.split(' - and last_id : ').length-1];
			if (new_id.length > 1) {
				localStorage.setItem("last_id",new_id);
			}
			
			
			var data_without_id = data.split(' - and last_id : ')[0];
			var shell_output = "";
			var gpio_pins_status = "0000000000";
			if (data_without_id.length > 0){
				var messages = data_without_id.split('{split_messages}');
				for (i = 0; i < messages.length; i++) {
					if (i==messages.length-1){
						gpio_pins_status = messages[i].split("{GpioCode}")[1];
					}
					var test = messages[i].split("{GpioCode}")[0].split('{separationdesmessage}');
					for (j = 0; j < test.length; j++) {
						if (test[i].length > 3){
							shell_output += "<br>" + test[i];
						}					
					}
				}
			}


			var temp = gpio_pins_status.slice(0,2)+"°C";
			var RPi1 = gpio_pins_status.charAt(2);
			var RPi2 = gpio_pins_status.charAt(3);
			var RPi3 = gpio_pins_status.charAt(4);
			var RPi4 = gpio_pins_status.charAt(5);
			var ventilo1 = gpio_pins_status.charAt(6);
			var ventilo2 = gpio_pins_status.charAt(7);
			var ventilo3 = gpio_pins_status.charAt(8);
			var ventilo4 = gpio_pins_status.charAt(9);
			
			var components_array = [RPi1,RPi2,RPi3,RPi4,ventilo1,ventilo2,ventilo3,ventilo4];
	


			for (i = 0; i < components_array.length; i++) {
				if(components_array[i]=="1") {
					//set button i color to green
				} else {
					//set button i color to red
				}
			}


			if(temp!="00°C" && temp!="..°C"){
				$("#temperature").html(temp);
			}
			
			if(document.getElementById("loading")) {
				if (shell_output.length > 1) {
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
