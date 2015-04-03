var gpreq;






function sendRequest(){
    if (window.XMLHttpRequest){
        gpreq = new XMLHttpRequest();
    }else{
        gpreq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    var gpgame_id = document.getElementById("gid").value
    gpreq.onreadystatechange = handleResponse;
    gpreq.open("GET","/twentyFour/get_progress/"+gpgame_id,true);
    gpreq.send();
}

function handleResponse(){
    if (gpreq.readyState != 4 || gpreq.status != 200){
        return;
    }
    var plist = document.getElementById("progress_list");

    while (plist.hasChildNodes()){
        plist.removeChild(plist.firstChild);
    }
    var states = JSON.parse(gpreq.responseText);
    for (var i = 0; i < states.length; ++i){
        var id = states[i].fields.player;
        var progress = states[i].fields.progress;
        var point = states[i].fields.point
        //need to extract player picture and score
        var newProgress = document.createElement("tr");
        newProgress.innerHTML = progress + "sets solved" +"        "+ " current points: "+ point;
        plist.appendChild(newProgress)
    }
}

window.setInterval(sendRequest,1500);
