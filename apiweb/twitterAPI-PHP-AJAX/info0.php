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
$consumer_key = "RfguuVtq4T9Xz3PeYBc2sCIEV";
$consumer_secret = "Ov3dDApzrFpckTcEAMUmwvA9k7Y9SEnDHg7T0AlBEAvTOVNGuI";
$oauth_token = "709007460401606656-cbFxI1puyVymLQjd2psTJ6QjFa9l47F";
$oauth_token_secret = "30ugVkeKsYFuqeMKmuq2IdaOa6TGkVYSPuobWTVGTW9eY";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
