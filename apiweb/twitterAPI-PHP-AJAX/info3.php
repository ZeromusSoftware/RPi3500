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
$consumer_key = "LT2r3HbTnJgGYRGsVSGrxLRma";
$consumer_secret = "7S7CZznOm76yNRRWsN5ibE959AJupZHWvSY93yl9nxF0IgcbPt";
$oauth_token = "709007460401606656-OpWAdtJG6lupZ1fkKeFU9bp0ylUkNeT";
$oauth_token_secret = "Lv5QyZMDL7o0ts0pGUsWTzUtghaVXC0YUeB8xX3PDGLUD";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
