<?php
session_start();
include('functions.php');

$url = 'https://api.twitter.com/1.1/direct_messages/new.json';
$requestMethod = "POST";
$userID  = "709011390850330624"; // Rasta BerryPi's ID


if (isset($_POST['text'])) {
	$text = $_POST['text'];
} else {
	$text = 'test';
}

$postfield = "?user_id=$userID&text=$text";

$twitter = new TwitterAPIExchange($settings);
$string = json_decode($twitter->buildOauth($url, $requestMethod)
			->setPostfield($postfield)
			->performRequest(),$assoc = TRUE);

if($string["errors"][0]["message"] != "") {
	echo "<h3>Sorry, there was a problem.</h3><p>Twitter returned the following error message:</p><p><em>".$string[errors][0]["message"]."</em></p>";
	exit();
}


?>