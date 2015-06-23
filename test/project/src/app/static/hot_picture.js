$(function () {
	var tmp = [],
		hum = [],
		t;

    try{
	
	    var table1 = document.getElementById("data_table");
        for (var i = 1; i <= table1.rows.length; i++) {
        alert("tmp"+i);
           var tt = document.getElementById("tmp"+i);
           if( tt == null){
            alert(tt.value);
           }else{
            tmp.push(tt.value);
           }

      		var hh = document.getElementById("hum"+i);
  		  if( hh == null){
                    alert(hh.value);
           }else{
                    hum.push(hh.value);
           }
			//	t = table1.rows[i].cells[2].innerHTML;
			//	hum.push(2);
        	}
      }catch(err){
      	alert(err)
      }
  

	var data = [{
		name: 'TMP',
		value: tmp,
		color: '#0d8ecf',
		line_width: 2
	}, {
		name: 'HUM',
		value: hum,
		color: '#ef7707',
		line_width: 2
	}];
	var labels = ["2012-08-01", "2012-08-02", "2012-08-03", "2012-08-04", "2012-08-05", "2012-08-06"];
	var line = new iChart.LineBasic2D({
		render: 'canvasDiv',
		data: data,
		align: 'center',
		title: 'ichartjs官方网站最近5天流量趋势',
		subtitle: '平均每个人访问2-3个页面(访问量单位：万)',
		footnote: '数据来源：模拟数据',
		width: 800,
		height: 400,
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
			offsetx: -80, //设置x轴偏移，满足位置需要
			border: true
		},
		crosshair: {
			enable: true,
			line_color: '#62bce9'
		},
		sub_option: {
			label: false,
			point_hollow: false
		},
		coordinate: {
			width: 640,
			height: 240,
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
				scale_space: 10,
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
});
