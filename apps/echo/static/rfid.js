 var sock = new SockJS('http://localhost:5000/rfid_listener');
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
       data_array = data.split(",")
      for (var i=0,len=data_array.length; i<len; i++){
        line = data_array[i].split(":")
 	    $('#chat-content').val(function (i, text) {
            return text + 'cardID: ' + line[0] + '-> triggerID: ' + line[1] + '\n';
 	    });
      }
};
// 	var data_table = document.getElementById("data_table");
//	tr_para.setAttribute('onmouseover', "this.style.backgroundColor='#ffff66';");
//	tr_para.setAttribute('onmouseout', "this.style.backgroundColor='#d4e3e5';");
//    alert("ok")
//      data = e.data
//      data = data.split(",")
//      for (var i=0,len=data.length; i<len; i++){
//
//        var tr_para = document.createElement("tr");
//        data = data[i].split(":")
//
//        var nodeid = document.createElement("td");
//		nodeid.innerHTML = data[0];
//		tr_para.appendChild(nodeid);
//
//		var tmp = document.createElement("td");
//		tmp.innerHTML = data[1];
//		tr_para.appendChild(tmp);
//
//		data_table.appendChild(tr_para);
//      }
// };
