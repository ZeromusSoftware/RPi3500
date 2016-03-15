<?php
session_start();
include('functions.php');

$url = 'https://api.twitter.com/1.1/direct_messages.json';
$requestMethod = "GET";
$userID  = "709011390850330624"; // Rasta BerryPi's ID


if (isset($_GET['count'])) {
	$count = $_GET['count'];
} else {
	$count = 20;
}

$getfield = "?user_id=$userID&count=$count";

$twitter = new TwitterAPIExchange($settings);
$string = json_decode($twitter->setGetfield($getfield)
			->buildOauth($url, $requestMethod)
			->performRequest(),$assoc = TRUE);

if($string["errors"][0]["message"] != "") {
	echo "<h3>Sorry, there was a problem.</h3><p>Twitter returned the following error message:</p><p><em>".$string[errors][0]["message"]."</em></p>";
	exit();
}


/*---------------------VIEW------------------------------------------------*/
foreach($string as $items)
{
	echo "Time and Date: ".$items['created_at']."<br />";
	echo "Message: ". $items['text']."<br />";
	echo "Posted by: ". $items['user']['screen_name']."<br />";
	/*echo "Screen name: ". $items['user']['screen_name']."<br />";
	echo "Followers: ". $items['user']['followers_count']."<br />";
	echo "Friends: ". $items['user']['friends_count']."<br />";
	echo "Listed: ". $items['user']['listed_count']."<br /><hr />";*/
}

?>
