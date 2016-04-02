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


if (isset($_GET['info']) /*and int($_GET(['info'])) % 3) < 3*/ ) {

	//'.string(int($_GET['info']) % 3).'

	//require('../info1.php'); // to load $settings and TwitterAPIExchange

	/* URL and settings from http://dev.twitter.com/rest/public */
	/*$url = 'https://api.twitter.com/1.1/direct_messages.json';
	$getfield = '?count=5';
	$requestMethod = 'GET';*/

	/* Create a TwitterOAuth object with consumer tokens */
	/*$twitter = new TwitterAPIExchange($settings);
	echo $twitter->setGetfield($getfield)
	    ->buildOauth($url, $requestMethod)
	    ->performRequest(); // to return data to AJAX*/

	echo $_GET(['info'])

} else {

	echo 'borgne';

}

?>
