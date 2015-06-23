var sock = new SockJS('http://localhost:5000/light');
//var sock = new SockJS('http://localhost:5000/rfid_listener');
// Open the connection
 sock.onopen = function () {
 	console.log('open');
 };

 // On connection close
 sock.onclose = function () {
 	console.log('close');
 };

 // On receive message from server
 sock.onmessage = function (e) {
 	   data = e.data
};

function id1(){
    sock.send('1');
//    alert("id1");
}

function id2(){
    sock.send('2');
//    alert("id2");
}

function id3(){
    sock.send('3');
//    alert("id3");
}

function id0(){
    sock.send('0');
//    alert("id0");
}
//sock.send('test');
//sock.close();