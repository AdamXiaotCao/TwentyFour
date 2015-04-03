//var cendReq;
var count = 0;
function endGame(){
   alert ("7 seconds passed");

//   if (window.XMLHttpRequest){
//       cendReq = new XMLHttpRequest();
//   } else{
//       cendReq = new ActiveXObject("Microsoft.XMLHTTP");
//   }
   var mygame_id = document.getElementById("gid").value
   var url = "/twentyFour/end_game/"+mygame_id;
   window.location = url
//    cendReq.onreadystatechange = handleEnd;
//   cendReq.open("GET","/twentyFour/end_game/"+mygame_id,true);
//   cendReq.send();
}
//function handleEnd(){
//    if (creq.readyState != 4 || creq.status != 200){
//        count = 0;
//        return;
//    }
//
//    alert("Game is ended!! Redirect to the result page");
//}
window.setInterval(endGame,7000);
