/*
Add these on your HTML page :
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="js/api.js"></script>
*/

var reloadTime = 1000;
var scrollBar = false;

function getMessages() {
    // On lance la requête ajax
    $.getJSON('/phpscripts/get-message.php', function(items) {
            /* On vérifie que error vaut 0, ce
            qui signifie qu'il n'y aucune erreur */
            if($string["errors"][0]["message"] == "") {
                // On intialise les variables pour le scroll jusqu'en bas
                // Pour voir les derniers messages
                var container = $('#text');
                var content = $('#messages_content');
                var height = content.height()-500;
                var toBottom;
                
                // Si avant l'affichage des messages, on se trouve en bas,
                // alors on met toBottom a true afin de rester en bas               
                // Il faut tester avant affichage car après, le message a déjà été
                // affiché et c'est aps facile de se remettre en bas :D
                if(container[0].scrollTop == height)
                    toBottom = true;
                else
                    toBottom = false;

                $("#text").html($items['text']);

                // On met à jour les variables de scroll
                // Après avoir affiché les messages
                content = $('#messages_content');
                height = content.height()-500;
                
                // Si toBottom vaut true, alors on reste en bas
                if(toBottom == true)
                    container[0].scrollTop = content.height();  
  
                // Lors de la première actualisation, on descend
                if(scrollBar != true) {
                    container[0].scrollTop = content.height();
                    scrollBar = true;
                }   
            } else if($string["errors"][0]["message"] != "") {
                /* Si error vaut unlog, alors l'utilisateur connecté n'a pas
                de compte. Il faut le rediriger vers la page de connexion */
                $("#text").html("<h3>Sorry, there was a problem.</h3><p>Twitter returned the following error message:</p><p><em>".$string[errors][0]["message"]."</em></p>");
                //$(location).attr('href',"api.php");
            }
    });
}


function postMessage() {
    // On lance la requête ajax
    // type: POST > nous envoyons le message
    // On encode le message pour faire passer les caractères spéciaux comme +
    var message = encodeURIComponent($("#message").val());
    $.ajax({
        type: "POST",
        url: "/phpscripts/post-message.php",
        data: "message="+message,
        success: function(msg){
            // Si la réponse est true, tout s'est bien passé,
            // Si non, on a une erreur et on l'affiche
            if(msg == true) {
                // On vide la zone de texte
                $("#message").val('');
                $("#responsePost").slideUp("slow").html('');
            } else
                $("#responsePost").html(msg).slideDown("slow");
            // on resélectionne la zone de texte, en cas d'utilisation du bouton "Envoyer"
            $("#message").focus();
        },
        error: function(msg){
            // On alerte d'une erreur
            alert('Erreur');
        }
    });
}


// Au chargement de la page, on effectue cette fonction
$(document).ready(function() {
    // On vérifie que la zone de texte existe
    // Servira pour la redirection en cas de suppression de compte
    // Pour ne pas rediriger quand on est sur la page de connexion
    if(document.getElementById('message')) {
        // actualisation des messages
        window.setInterval(getMessages, reloadTime);
        // on sélectionne la zone de texte
        $("#message").focus();
    }
});

