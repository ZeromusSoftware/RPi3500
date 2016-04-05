<?php
/*********************************************************
 * Feature to get last direct messages
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/


if (isset($_GET['info'])) {


	require('../info'.$_GET['info'].'.php'); // to load $settings and TwitterAPIExchange
	
	$last_id = $_GET['last_id'];

	/*URL and settings from http://dev.twitter.com/rest/public*/
	$url = 'https://api.twitter.com/1.1/direct_messages.json';
	$getfield = '?count=10&since_id='.$last_id;
	$requestMethod = 'GET';

	/* Create a TwitterOAuth object with consumer tokens */
	$twitter = new TwitterAPIExchange($settings);
	$response = $twitter->setGetfield($getfield)
	    ->buildOauth($url, $requestMethod)
	    ->performRequest(); // to return data to AJAX

	$tweets = json_decode($response,true);
	$last_messages = "";
	$last_id = "";
	if (sizeof($tweets) > 0) {
		foreach ($tweets as $tweet) {
			$last_messages = $last_messages."</br></br>".$tweet['text'];
		}

		$last_id = $tweets[0]['id'];
	}
	echo $last_messages." - and last_id : ".$last_id;
} else {

	echo 'borgne';

}

?>
