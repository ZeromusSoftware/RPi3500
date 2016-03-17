<?php
/*------------------------------------------------------*/
/*--------------------- GET LAST TWEETS ----------------*/
/*------------------------------------------------------*/


/* To load all important data like $settings
   and to  use TwitterAPIExchange            */
require('info.php'); 

    
$url = 'https://api.twitter.com/1.1/direct_messages.json';
$getfield = '?count=5';
$requestMethod = 'GET';

$twitter = new TwitterAPIExchange($settings);
/* Echo to return data to AJAX and JQuery */
echo $twitter->setGetfield($getfield)
    ->buildOauth($url, $requestMethod)
    ->performRequest();


?>
