
var creq;

function sendcRequest(){
    if (window.XMLHttpRequest){
        creq = new XMLHttpRequest();
    }else{
        creq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    var cgame_id = document.getElementById("gid").value;
    creq.onreadystatechange = handlecResponse;
    creq.open("GET","/twentyFour/check_game/"+cgame_id,true);
    creq.send();
}

function handlecResponse(){
    if (creq.readyState != 4 || creq.status != 200){
        return;
    }
    var cgame = JSON.parse(creq.responseText)[0];
    var cstatus = cgame.fields.status
    if (cstatus=="ONGOING"){
//        alert("game is ongoing!");
//        var cbutton = document.getElementById("submitbt");
//        cbutton.disabled=false;
        location.reload()
    }else{

        return
    }
}
window.setInterval(sendcRequest,1500);
