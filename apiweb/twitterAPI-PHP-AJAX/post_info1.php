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
$consumer_key = "cA7dWor1XujGYNjzbPvkVnWK2";
$consumer_secret = "pIiyEkPCE0TZ6Gh4vFlPCQgKcablFErXVogeve7ZWDNkInC1MD";
$oauth_token = "709007460401606656-zfbM9NWCzGMYlCaSttQsYEkfV13KtFO";
$oauth_token_secret = "TxyoB4mqaj1Av0czdOlI2AkSeTDzBy7PuslLzkRKbmxVv";

$settings = array(
    'oauth_access_token' => $oauth_token,
    'oauth_access_token_secret' => $oauth_token_secret,
    'consumer_key' => $consumer_key,
    'consumer_secret' => $consumer_secret
);

/*---- From https://github.com/J7mbo/twitter-api-php ---*/
require_once('TwitterAPIExchange.php');

?>
