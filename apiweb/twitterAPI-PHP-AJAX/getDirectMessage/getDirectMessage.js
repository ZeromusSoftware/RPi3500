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

	// number of calls is stored in localStorage so you can switch app between two calls
	if (!localStorage.getItem("calls")) {
		localStorage.setItem("calls","1"); 
	}
	var nbrOfCalls = +localStorage.getItem("calls"); // "+" converts string to integer
	
	if (nbrOfCalls>=7){ // 6 different get apps are used
		localStorage.setItem("calls","1");
		nbrOfCalls=1;
	} else {
		localStorage.setItem("calls", (nbrOfCalls+1).toString());
	}
	var appToUse = nbrOfCalls.toString();
	
	// last id is stored so you can get only new messages
	if (!localStorage.getItem("last_id") || localStorage.getItem("last_id")=="0") {
		localStorage.setItem("last_id","717044642315968515");
	}
	var last_id_printed = localStorage.getItem("last_id");
	
	
	$.ajax({
		url: '/twitterAPI-PHP-AJAX/getDirectMessage/getDirectMessage.php', 
		type: 'GET',
		data:'info='+ appToUse + "&last_id=" + last_id_printed,
		success: function(data) { // executed if getDirectMessage.php didn't return any error

			// storing the new last id recieved
			var new_id = data.split(' - and last_id : ')[data.split(' - and last_id : ').length-1];
			if (new_id.length > 1) {
				localStorage.setItem("last_id",new_id);
			}
			
			// spliting new messages to get gpio_code (containing temperature and pins status) and message text
			var data_without_id = data.split(' - and last_id : ')[0];
			var shell_output = "";
			var gpio_pins_status = "xxxxxxxxxx";
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

			// spread pins statuses and temperature from the gpio_code in corresponding variables
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
	
			// if an actual gpio_code has been recieved ( <=> a message has been recieved)
			if (gpio_pins_status != "xxxxxxxxxx") {

				for (i = 0; i < components_array.length; i++) { // for each component
					
					(function (i) { // for loops closure problem in javascript

						var k = (i+1).toString(); // to transform i into a variable that can be used in IDs with 'button'+k

  						if(components_array[i]=="1") {
       							
       							document.getElementById("button" + k).style.background='green'; // to change k button color to green
       							document.getElementById("button" + k).name='0'; // to change k button name corresponding to green
						

 	 					} else {

       							document.getElementById("button" + k).style.background='red'; // to change k button color to red
       							document.getElementById("button" + k).name='1'; // to change k button name corresponding to red
  						}
						
					// each time replacing the onclick function by the one which will change the on/off status of the component
						var state = document.getElementById("button" + k).getAttribute("name");
						var action = document.getElementById("button" + k).getAttribute("onclick");
						var l = action.length-11;
						var gpio = action.substring(19,l);
						document.getElementById("button" + k).onclick = function() {
							turnOnOffComponent(gpio,state,this.id);
						}

					}).call(this, i);

				}

				// showing the current temperature in the box
				$("#temperature").html(temp);

			}
			// showing the messages sent back by the cluster
			if(document.getElementById("loading")) { // if it is the first message to show
				if (shell_output.length > 1) {

				var d = new Date();
				var h = d.getHours();
				var m = d.getMinutes();
				var s = d.getSeconds();
				var day = d.getDate();
				var M = +d.getMonth()+1;
				var Y = d.getFullYear();
				
				var date_list = [M.toString(),day.toString(),h.toString(),m.toString(),s.toString()];
				for (i = 0; i < date_list.length; i++) {
					if(date_list[i].length == 1) {
						date_list[i] = "0" + date_list[i];
					}
				}

					$("#text").html("<div class='get'>" + shell_output + "</div>");

				}else { // if there are now messages to show
					$("#text").html("<div class='get'>enter a command..</div>");
				}
			} else {
				if (shell_output.length > 1) {


				var d = new Date();
				var h = d.getHours();
				var m = d.getMinutes();
				var s = d.getSeconds();
				var day = d.getDate();
				var M = +d.getMonth()+1;
				var Y = d.getFullYear();
				
				var date_list = [M.toString(),day.toString(),h.toString(),m.toString(),s.toString()];
				for (i = 0; i < date_list.length; i++) {
					if(date_list[i].length == 1) {
						date_list[i] = "0" + date_list[i];
					}
				}


					$("#text").append("<div class='get'>" + shell_output + "</div>");
				}
			}
		},
		error: function(data) {
			alert("Error ajax getMessage");
		}	
	});
}
