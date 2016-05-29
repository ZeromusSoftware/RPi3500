<!doctype html>
<!--------------------------------------------------------
 ! Adamant API's main page
 !  
 ! @package  TwitterAPI-PHP-AJAX
 ! @author   Bastien Pederencino <bpderencino@legtux.org>
 ! @license  GNU General Public License 2
 ! @version  0.1.0
 ! @link     http://github.com/ZeromusSoftware/RPi3500
 -------------------------------------------------------->


<html lang='fr'>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<meta name="description" content="RPi Control Chamber" />
		<link rel="stylesheet" href="style.css" />
		<title>RPi Control Chamber - Adamant</title>
	</head>
	<body>
                       
		<div id="container">
			<table class="chat"><tr>        
				<!-- message area -->
				<td valign="top" id="text-td">
					<?php include('getDirectMessage/divToInclude.php'); ?>
				</td>
			</tr></table>

			<!-- Text area -->
			<a name="post"></a>
			<table class="post_message"><tr>
				<td>
					<?php include('postDirectMessage/divToInclude.php'); ?>
					<div id="responsePost" style="display:none"></div>
				</td>
			</tr></table>
			
		</div>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script src="getDirectMessage/getDirectMessage.js"></script>
		<script src="postDirectMessage/postDirectMessage.js"></script>
		<script src="adamant.js"></script>
	</body>
</html>
