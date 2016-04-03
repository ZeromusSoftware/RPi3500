<?php
/*********************************************************
 * Feature to send a new direct message
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/

if (isset($_POST['info'])){
	require('../info'.$_POST['info'].'.php'); // to load $settings and TwitterAPIExchange
} else {
	require('../info0.php');
}



/* URL and settings from http://dev.twitter.com/rest/public */
$userID  = "709011390850330624"; // Rasta BerryPi's ID
if (isset($_POST['message'])) {
	$text = $_POST['message'];
} else {
	$text = 'test';
}
$postfields = array(
    'user_id' => $userID, 
    'text' => $text
);
$url = 'https://api.twitter.com/1.1/direct_messages/new.json';
$requestMethod = 'POST';

/* Create a TwitterOAuth object with consumer tokens */
$twitter = new TwitterAPIExchange($settings);
echo $twitter->buildOauth($url, $requestMethod)
    ->setPostfields($postfields)
    ->performRequest(); // to return data to AJAX


?>
