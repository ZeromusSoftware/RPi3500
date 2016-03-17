<?php
/*------------------------------------------------------*/
/*--------------------- POST NEW TWEETS ----------------*/
/*------------------------------------------------------*/


/* To load all important data like $settings
   and to  use TwitterAPIExchange            */
require('info.php'); 


$userID  = "709011390850330624"; // Rasta BerryPi's ID

if (isset($_POST['message'])) {
	$text = $_POST['message'];
} else {
	$text = 'test';
}


$url = 'https://api.twitter.com/1.1/direct_messages/new.json';
$postfields = array(
    'user_id' => $userID, 
    'text' => $text
);
$requestMethod = 'POST';


$twitter = new TwitterAPIExchange($settings);
/* Echo to return data to AJAX and JQuery */
echo $twitter->buildOauth($url, $requestMethod)
    ->setPostfields($postfields)
    ->performRequest();


?>
