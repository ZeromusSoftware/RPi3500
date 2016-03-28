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
$consumer_key = "y2EAVgGStHUf3f8Gz24UIgzdf";
$consumer_secret = "YEFdyhf1NQBQ8QTY8wknVcQsHOLjvut030Y1GxHpIe69XpJTPR";
$oauth_token = "709007460401606656-7MCCrLjyaMWenz1Yt95dB9eX7n751j4";
$oauth_token_secret = "ASppc76cUDrq5fcQxKmvafUIt6jNHF9Egv0i62z0r2Xax";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
