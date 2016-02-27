<?php  
	// Adamant web page
		
	function powerButton($value) = {
		if ($value == 1) {
			$buttonValue = 'ON';
		}
		else if ($value == 0) {
			$buttonValue = 'OFF';
		}
		return '
			<script>  
				function borgne'.$value.'() {  
					window.location="apirpi.php?jarvis=borgne'.$value.'";  
				}  
			</script>  

			<input type="button" class="power"  value="Power '.$buttonValue.'" onClick="borgne'.$value.'()" /> 	
		';
	}
	
	$powerONButton = powerButton(1);
	$powerOFFButton = powerButton(0);
	
	echo $powerONButton;
	echo $powerOFFButton;
	
	if (isset($_GET["rpi"])){
		$rpi = $_GET["rpi"];
		echo '<h2>'.$rpi.'</h2>';
	}
?> 
