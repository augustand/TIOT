var sock = new SockJS('http://localhost:5000/xbee'); //sock初始化
// Function for sending the message to server
var id_node = 1;
var id_hum = 1;
var id_tmp = 1;
var id_show = 1;
var tmp = [],hum = [];
var i;
var num = 0;

var status;//状态网页显示条数
sock.onopen = function() {
	id_node = 1;
	id_hum = 1;
	id_tmp = 1;
	id_show = 1;
	tmp = [];
	hum = [];
	i = 0;
	console.log('open');
	status = 0;

	num = 0;
};

// On connetion close
sock.onclose = function() {
	id_node = 1;
	id_hum = 1;
	id_tmp = 1;


	console.log('close');
};



var pv = [],
	ip = [],
	t;

// // On receive message from server
sock.onmessage = function(e) {

	status++;


	// Get the content
	var content = JSON.parse(e.data);
	if(content[0].tmp == undefined){
		content[0].tmp = '20';
	}



	if(content[0].hum == undefined){
		content[0].hum = '65';
	}


	i = i+1;


	// Append the text to text area (using jQuery)
	$('#chat-content').val(function(i, text) {
		return text+'设备id ' + content[0].nodeid + " 温度:" + content[0].tmp + ' 湿度:' + content[0].hum + '\n';
	});

	var data_table = document.getElementById("data_table");

	var tr_para = document.createElement("tr");
	tr_para.setAttribute('onmouseover', "this.style.backgroundColor='#ffff66';");
	tr_para.setAttribute('onmouseout', "this.style.backgroundColor='#d4e3e5';");





	var nodeid = document.createElement("td");
	nodeid.setAttribute("id", "nodeid" + (id_node++));
	nodeid.innerHTML = content[0].nodeid;
	tr_para.appendChild(nodeid);

	var tmp = document.createElement("td");
	tmp.setAttribute("id", "tmp" + (id_tmp++));
	tmp.innerHTML = content[0].tmp;
	tr_para.appendChild(tmp);

	var hum = document.createElement("td");
	hum.setAttribute("id", "hum" + (id_hum++));
	hum.innerHTML = content[0].hum;
	tr_para.appendChild(hum);




	var num1 = document.createElement("td");
	num1.setAttribute("id", "num" + (num++));
	num1.innerHTML = num;
	tr_para.appendChild(num1);



	data_table.appendChild(tr_para);



// d= document.getElementById("column").childNodes;
// for(var i=0 ;i < d.length; i++){

  //      document.getElementById("column").removeChild(d.item(i));
    //  }

	if(status == 30){


d= document.getElementById("data_table").childNodes;
document.getElementById("data_table").removeChild(d.item(2));

	   // id_node = 1;
		//id_tmp = 1;
		//id_hum = 1;
	    pv.shift();
	    ip.shift();
	    status = status -1;
		//i = 0;

	    }




	try {

		t = content[0].tmp;
		if (t != null) {
			t *= 1;
			pv.push(t);
		}

		t = content[0].hum;
		if (t != null) {
			t *= 1;
			ip.push(t);
		}

//		pv = data_handle(pv);
	//	ip = data_handle(ip);

		var data = [{
			name: '温度',
			value: pv,
			color: '#0d8ecf',
			line_width: 1
		}, {
			name: '湿度',
			value: ip,
			color: '#ef7707',
			line_width: 1
		}];
		var labels = ['01','02','03','04','05','06','07','08','09','10'];
		var line = new iChart.LineBasic2D({
			render: 'canvasDiv',
			data: data,
			align: 'center',
			title: '粮仓温湿度检测系统',
			subtitle: '随时变化的30个数据',//平均每个人访问2-3个页面(访问量单位：万)
			footnote: '数据来源：真实数据',
			width: 1300,
			height: 750,
			tip: {
				enable: true,
				shadow: true
			},
			legend: {
				enable: true,
				row: 1, //设置在一行上显示，与column配合使用
				column: 'max',
				valign: 'top',
				sign: 'bar',
				background_color: null, //设置透明背景
				offsetx: -5, //设置x轴偏移，满足位置需要
				border: true
			},
			crosshair: {
				enable: true,//true
				line_color: '#62bce9'
			},
			sub_option: {
				label: false,
				point_hollow: false
			},
			coordinate: {
				width: 1200,
				height: 600,
				axis: {
					color: '#9f9f9f',
					width: [0, 0, 2, 2]
				},
				grids: {
					vertical: {
						way: 'share_alike',
						value: 5
					}
				},
				scale: [{
					position: 'left',
					start_scale: 0,
					end_scale: 100,
					scale_space: 5,
					scale_size: 2,
					scale_color: '#9f9f9f'
				}, {
					position: 'bottom',
					labels: labels
				}]
			}
		});
		//开始画图
		line.draw();

	} catch (err) {
		alert(err)
	}

};

function sendMessage() {
	// Get the content from the textbox
	var message = $('#message').val();
	var username = $('#username').val();

	// The object to send
	var send = {
		message: message,
		username: username
	};
	// Send it now
	sock.send(JSON.stringify(send));
}



function data_handle(dec_list) {

	var sum = new Array();
	for(var x in dec_list){
		if(x  != 0){
			sum. push(parseInt(x));
		}
	}



	var index=0;
	for (var i=0;i<sum.length ;i++ ){
 		index=sum[i]+index;
	}

	if (index != 0 && sum.length != 0) {
			index = index / 2;//sum.length
	}


	for(var i =0; i < dec_list.length;i++){
		if(dec_list[i] == 0){
			dec_list[i]  = index;
		}
	}
		return dec_list;
	}


//function show() {
//	var hot_show = document.getElementById("hot_show");
//	if (hot_show != null) {
//		document.body.removeChild(hot_show);
//	}
//	id_show += 1;
//	var myScript = document.createElement("script");
//	myScript.type = "text/javascript";
//	myScript.src = "/static/hot_picture.js?" + Math.random();
//	myScript.id = "hot_show";
//	document.body.appendChild(myScript);
//}


