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
$consumer_key = "GSfig3tojJwkoQmMEN9GeGVth";
$consumer_secret = "VoqtQ0NvqA0BGunUJTvMHqZlQ4RLGB7WenOlPVouFjL9UEUjEv";
$oauth_token = "709007460401606656-ksP8JBTemcNr7DQrYNNZcozWGRY3b1k";
$oauth_token_secret = "DtdG0YeelyqWvkNQdiHHE9keryOSyuaTPcZBz6zrtRRyv";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
