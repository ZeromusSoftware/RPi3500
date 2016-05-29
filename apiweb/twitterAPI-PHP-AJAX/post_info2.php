<?php
/*********************************************************
 * All important data
 *  
 * @package  TwitterAPI-PHP-AJAX
 * @author   Bastien Pederencino <bpderencino@legtux.org>
 * @license  GNU General Public License 2
 * @version  0.1.0
 * @link     http://github.com/ZeromusSoftware/RPi3500
 ********************************************************/


session_start();

/*---------------- From http://apps.twitter.com---------*/
$consumer_key = "NbtHbQap7nSGk20csKmEvEpLi";
$consumer_secret = "CIq9WRd8CyhnVfM2SOSSPS63elXklQ2vGIuM3MALBYG90y4ZTc";
$oauth_token = "735446697724268545-Op2pZR4ce4ZcF49kbnNW44rRI5KBc2v";
$oauth_token_secret = "RFy1CYTghZY590vyIWlH4OOAF7xx7Bx4WksNEMtZwBk1t";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
