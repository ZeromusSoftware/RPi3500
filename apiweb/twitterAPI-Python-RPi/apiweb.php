<?php  
	// Adamant web page
		
	function powerButton($gpio,$valueChoice) = {
		$buttonSelected = (string)$gpio; 
		$buttonValue = (string)$valueChoice; //value 0 or 1
		}
		return '
			<script>  
				function switch'.$buttonSelected.$buttonValue.'() {  
					window.location="apirpi.php?switch=switch_'.$buttonSelected.'_'.$buttonValue.'";  
				}  
			</script>  

			<input type="button" class="power"  value="Power '.$buttonValue.' gpio '.$buttonSelected.'" onClick="switch'.$buttonSelected.$buttonValue.'()" /> 	
		';
	}
	
	$powerONButtonRPi0 = powerButton(0,1);
	$powerOFFButtonRPi0 = powerButton(0,0);
	$powerONButtonRPi1 = powerButton(1,1);
	$powerOFFButtonRPi1 = powerButton(1,0);
	$powerONButtonRPi2 = powerButton(2,1);
	$powerOFFButtonRPi2 = powerButton(2,0);
	$powerONButtonRPi3 = powerButton(3,1);
	$powerOFFButtonRPi3 = powerButton(3,0);
	$powerONButtonRPi4 = powerButton(4,1);
	$powerOFFButtonRPi4 = powerButton(4,0);
	
	echo $powerONButtonRPi0;
	echo $powerOFFButtonRPi0;
	echo $powerONButtonRPi1;
	echo $powerOFFButtonRPi1;
	echo $powerONButtonRPi2;
	echo $powerOFFButtonRPi2;
	echo $powerONButtonRPi3;
	echo $powerOFFButtonRPi3;
	echo $powerONButtonRPi4;
	echo $powerOFFButtonRPi4;
	
	if (isset($_GET["rpi"])){
		$rpi = $_GET["rpi"];
		echo '<h2>'.$rpi.'</h2>';
	}
?> 
