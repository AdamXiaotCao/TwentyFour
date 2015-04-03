
var preq;


function sendpRequest(){
    if (window.XMLHttpRequest){
        preq = new XMLHttpRequest();
    }else{
        preq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    var pgame_id = document.getElementById('gid');
    preq.onreadystatechange = handlepResponse;
    preq.open("GET","/twentyFour/get_players/"+pgame_id.value,true);
    preq.send();
}

function handlepResponse(){
    if (preq.readyState != 4 || preq.status != 200){
        return;
    }
    var list = document.getElementById("player_list");
//    var plist = document.getElementById("progress_list");
    while (list.hasChildNodes()){
        list.removeChild(list.firstChild);
//        plist.removeChild(plist.firstChild);
    }
    var players = JSON.parse(preq.responseText);
    for (var i = 0; i < players.length; ++i){
        var id = players[i]["pk"];
        var picture = players[i].fields.picture;
        var player = document.createElement("tr");
        player.innerHTML = "<img src=\"/twentyFour/photo/"+id+"\"" + "width=\"50\" height=\"50\">"+id;
//        var progress = document.createElement(("tr"));
//        progress.innerHTML = "0"
//        plist.appendChild(progress)
        list.appendChild(player);
    }
}
window.setInterval(sendpRequest,1500);
