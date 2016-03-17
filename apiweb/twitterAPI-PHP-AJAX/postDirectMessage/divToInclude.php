
<!--------------------------------------------------------
 ! Feature to send a new direct message
 !  
 ! @package  TwitterAPI-PHP-AJAX
 ! @author   Bastien Pederencino <bpderencino@legtux.org>
 ! @license  GNU General Public License 2
 ! @version  0.1.0
 ! @link     http://github.com/ZeromusSoftware/RPi3500
 -------------------------------------------------------->


<form action="web.php?code=12&page=12" method="" onsubmit="postMessage(); return false;">
	<input type="text" id="message" onsubmit="postMessage(); return false;" maxlength="255" />
	<input type="button" onclick="postMessage()" value="Send" id="button" />
</form>
