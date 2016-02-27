<?php
	// RPi server page
  
	if (isset($_GET["jarvis"])){
		$jarvis = $_GET["jarvis"];
		if ($jarvis == "borgne0") {
			exec("python /var/www/remotecontrol/python/apirpiOFF.sh");
			echo '<h2>Hop hop hop tout le monde debout!!</h2>';
			$hi = 'OFF';
			
		}
		else if ($jarvis == "borgne1") {
			exec("python /var/www/remotecontrol/python/apirpiON.sh");
			echo '<h2>Hop hop hop tout le monde debout!!</h2>';
			$hi = 'ON';
		}
		else {
			exec($jarvis);  
			echo '<h2>We are the champion!!</h2>';
			$hi = 'DONE';
		}  
	}

	$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi='.$hi;
	header('Location: '.$link);
	exit();
?> 
