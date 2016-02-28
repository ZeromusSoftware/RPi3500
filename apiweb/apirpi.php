<?php
	// RPi server page
  
	if (isset($_GET["jarvis"])){
		$jarvis = $_GET["jarvis"];
		if ($jarvis == "borgne0") {
			exec("bash /var/www/remotecontrol/python/apirpiOFF.sh");
			echo '<h2>Hop hop hop tout le monde au dodo!!</h2>';
			$hi = 'OFF';
			
		}
		else if ($jarvis == "borgne1") {
			exec("bash /var/www/remotecontrol/python/apirpiON.sh");
			echo '<h2>Hop hop hop tout le monde debout!!</h2>';
			$hi = 'ON';
		}
		else {
			exec($jarvis);  
			echo '<h2>We are the champions!!</h2>';
			$hi = 'DONE';
		}  

		$link = 'http://www.bpederencino.legtux.org/apiweb.php?rpi='.$hi;
		
	}
	else{
		$link = 'http://www.bpederencino.legtux.org/apiweb.php';
	}
	header('Location: '.$link);
	exit();
?> 
