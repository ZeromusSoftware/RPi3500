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
$consumer_key = "SiPQkTj5GiocCRIrQrCOwbBQH";
$consumer_secret = "hV6UdUeeYyrIYB0O75YNtOCH7xLeEceNXvwkmpcfazf2JaCi1U";
$oauth_token = "709007460401606656-ItbHykYQaoFujTOSrV1arYW4ko9WjvE";
$oauth_token_secret = "u4tXNG0Rl7iEBThKpUJ49ZQ0hUWM7935c1QNHhG2wFOUM";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
