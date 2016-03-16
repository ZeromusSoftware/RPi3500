<?php
/*------------------------------------------------------*/
/*--------------------- GET LAST TWEETS ----------------*/
/*------------------------------------------------------*/


session_start();

// To load all important data like :
// $consumer_key, $consumer_secret, $oauth_token, $oauth_token_secret
// and to  : require_once('twitteroauth/src/TwitterOAuth.php');
require('info.php'); 


$connexion = new TwitterOAuth($consumer_key, $consumer_secret, $oauth_token, $oauth_token_secret);

$query = 'https://api.twitter.com/1.1/direct_messages.json?count=5';
$content = $connexion->get($query); // To send a query and get results

echo $content; // To return data to AJAX and JQuery

?>
