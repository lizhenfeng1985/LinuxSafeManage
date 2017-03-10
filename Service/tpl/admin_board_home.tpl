<html>
<head>
<title>HomeCount</title>

<script type="text/javascript" src="../static/fusioncharts/jquery-1.9.1.js"></script>
<script src="/static/fusioncharts/fusioncharts.js" type="text/javascript"></script>
<script src="/static/fusioncharts/fusioncharts.charts.js" type="text/javascript"></script>
<script src="/static/fusioncharts/fusioncharts.maps.js" type="text/javascript"></script>
<script src="/static/fusioncharts/fusioncharts.widgets.js" type="text/javascript"></script>
<script src="/static/fusioncharts/fusioncharts.gantt.js" type="text/javascript"></script>
<script src="/static/fusioncharts/fusioncharts.powercharts.js" type="text/javascript"></script>

<!-- 安全事件总体概况 -->
<script type="text/javascript">
  FusionCharts.ready(function(){
    var revenueChart = new FusionCharts(
	{
        "type": "column3d",
        "renderAt": "chartContainer",
        "width": "800",
        "height": "320",
        "dataFormat": "json",
        "dataSource":  {
        	"chart": {
           	 	"caption": "安全事件总体概况",
           	 	"subCaption": "分类统计图",
            	"xAxisName": "事件分类",
            	"yAxisName": "事件数量(个)",
				"showValues": "0",
				"canvasBgColor": "#ffffff",
				"showValues": "1",
				"showBorder": "1",
            	"theme": "fint"
         	},
        	"data": {{.Data}}
      	}
  	});
revenueChart.render();
})
</script>

</head>
<body bgcolor="#FFFFFF">
  <div id="chartContainer" align=center>Loading...</div>
</body>
</html>