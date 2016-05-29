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
$consumer_key = "MOOfGGz2nNNp787ck7fmpJJ6T";
$consumer_secret = "o3qc94zRF94nMiDXvA2m4QqbYzDY4JAC6dTHlAFZvccDuqYF42";
$oauth_token = "736545163393257473-g2jSwHygNDRhkeY7eKAbdrEaQ3B1Uk1";
$oauth_token_secret = "3X0N3m7r5aJq6AVqCBQIgmoGGs69libl3BcLtA8kwRflV";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
