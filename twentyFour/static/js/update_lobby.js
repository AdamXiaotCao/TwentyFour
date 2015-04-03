var req;

function sendRequest(){
    if (window.XMLHttpRequest){
        req = new XMLHttpRequest();
    }else{
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET","/twentyFour/get_games",true);
    req.send();
}

function handleResponse(){
    if (req.readyState != 4 || req.status != 200){
        return;
    }
    var list = document.getElementById("game_list");
    while (list.hasChildNodes()){
        list.removeChild(list.firstChild);

    }

    var games = JSON.parse(req.responseText);

    for (var i = 0; i < games.length; ++i){
        var id = games[i]["pk"];

        var newGame = document.createElement("li");
        newGame.innerHTML = "hey appending!!"
        newGame.innerHTML = "<a href=/twentyFour/join_multigame/"+ id+ ">Join!</a>"+id;
        list.appendChild(newGame)
    }
}
window.setInterval(sendRequest,1500);
