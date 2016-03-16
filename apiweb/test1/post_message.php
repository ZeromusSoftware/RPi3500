<?php
/*------------------------------------------------------*/
/*--------------------- POST NEW TWEETS ----------------*/
/*------------------------------------------------------*/


session_start();

// To load all important data like :
// $consumer_key, $consumer_secret, $oauth_token, $oauth_token_secret
// and to  : require_once('twitteroauth/src/TwitterOAuth.php');
require('info.php'); 


$connexion = new TwitterOAuth($consumer_key, $consumer_secret, $oauth_token, $oauth_token_secret);


$userID  = "709011390850330624"; // Rasta BerryPi's ID
if (isset($_POST['message'])) {
	$text = $_POST['message'];
} else {
	$text = 'test';
}
$postfield = '?user_id='.$userID.'&text='.$text;


$query = 'https://api.twitter.com/1.1/direct_messages/new.json'.$postfield;
$content = $connexion->post($query); // To send a query

echo $content; // To return data to AJAX and JQuery

?>
