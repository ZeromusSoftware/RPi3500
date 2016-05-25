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
$consumer_key = "IGPszw96ygbTkTl3LbrQk5pDN";
$consumer_secret = "dZuPDNquqTRovSE95UZZh5eUyZ7eingXbCOF0lrb98L9VCW2Bp";
$oauth_token = "709007460401606656-1mKzPApbPYfEdBrIcbwD1noMJ0L7tQP";
$oauth_token_secret = "Mpjyg8udyif8wz3IeSrHT0APzVcltFMRkxmeG6mpXq62z";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
