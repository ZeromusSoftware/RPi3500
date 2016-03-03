<?php
	// RPi server page
  
	if (isset($_GET["switch"])){

		$switch = $_GET["switch"];

		if ($switch == "switch_0_0"){
			exec("bash /var/www/remotecontrol/python/apirpiOFF.sh");
			echo '<h2>Hop hop hop tout le monde au dodo!!</h2>';
			$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi=Everything_is_OFF';
		}
		else if ($switch == "switch_0_1"){
			exec("bash /var/www/remotecontrol/python/apirpiON.sh");
			echo '<h2>Hop hop hop tout le monde debout!!</h2>';
			$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi=Everything_is_ON';
		}
		else{
			$gpio = $action[7];
			$mode = $switch[9];

			exec("gpio mode ".$gpio." out;"); //set mode to output
			exec("gpio write ".$gpio." ".$mode.";"); //turn on/off GPIO
			echo 'Debout ! Couché !';
			$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi='.$switch;
		}
	}
	else if (isset($_GET["task"])){
		$task = $_GET["task"];
		exec($task);  
		echo '<h2>We are the champions!!</h2>';
		$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi=DONE';
	}
	else{
		$link = 'http://www.bpederencino.legtux.org/apiweb.php';
	}
	header('Location: '.$link);
	exit();
?> 
