//测试数据

var ORDERLIST = [{
    id:'SE000010325',
    time: '2016.3.24',
    seller: 'ZaneXiao',
    amount: 66.2,
    state: 1,
    imgsrc: ['http://img1.imgtn.bdimg.com/it/u=1371246895,4061054626&fm=206&gp=0.jpg']
},
{
    id: 'SE000010510',
    time: '2016.3.22',
    seller: 'EowinYe',
    amount: 99.8,
    state: 2,
    imgsrc: ['http://d.hiphotos.baidu.com/image/h%3D200/sign=201258cbcd80653864eaa313a7dca115/ca1349540923dd54e54f7aedd609b3de9c824873.jpg']
},
{
    id: 'SE000010296',
    time: '2016.3.21',
    seller: 'ABC',
    amount: 12.5,
    state: 3,
    imgsrc: ['http://img2.imgtn.bdimg.com/it/u=355596720,3737965610&fm=206&gp=0.jpg']
}
];

var ORDERS = '{\
        "id": "SE000010325",\
        "time": "2016.3.24",\
        "user":"ZaneXiao",\
        "state": "NotDel",\
        "amount": 664.8,\
        "content": [\
            {\
                "title": "云恋酒店（不含早）",\
                "quantity":2,\
                "amount": 576.0,\
                "imgsrc": "http://www.cysz6.com/upload/hotel/1305/29/28664d284e439a97cbd622d2be6d35d9.jpg"\
            },\
            {\
                "title": "会员增值业务",\
                "quantity": 1,\
                "amount": 88.8,\
                "imgsrc": "http://img4q.duitang.com/uploads/item/201405/14/20140514113612_vTyFa.jpeg"\
            }\
        ],\
        "flow": [\
            {\
                "time": "2016.3.21 14:11",\
                "summary":"买家zyy已付款"\
            },\
            {\
                "time": "2016.3.22 00:03",\
                "summary": "卖家YunlianHotel确认订单"\
            },\
            {\
            "time": "2016.3.22 00:04",\
                "summary": "卖家YunlianHotel确认发货"\
            },\
            {\
                "time": "2016.3.25 19:52",\
                "summary": "买家zyy确认收货,交易完成"\
            }\
        ]\
    }';

//var COMPLAINTS = {
//    "SE000010325": {
//        id: "SE000010325",
       
//    }
//};

//测试数据-结束

//var StateType={
//    "NotPay":"待付款",
//    "NotDel":"待发货",
//    "Delivery":"已发货",
//    "Success":"交易成功",
//    "NotRef":"待退款",
//    "Refund":"已退款",
//    "Compl":"投诉中"
//};

var StateType = ["待付款","待发货", "已发货","交易成功","待退款","已退款", "投诉中"];


function post(URL, PARAMS, f) {
    $.ajax({
        type: "POST",
        url: URL,
        data: JSON.stringify(PARAMS),
        cache: false,
        // async: false,
        contentType: "application/json",
        dataType: "json",
        success: function (data) {
            f(data);
        }
    });
}

function addOrder(tr,d)
{
    tr.append("td").html("");
    //订单编号
    var td = tr.append("td");
    td.append("a").html(d.id);
    td.append("br");
    td.append("small").html(d.time);
    //商品
    td = tr.append("td");
    var ul = td.append("ul").attr("class", "list-inline");
    for (var p in d.imgsrc)
    {
        ul.append("li").append("img")
            .attr("src", d.imgsrc[p])
            .style("width", "50px")
            .style("height", "50px");
    }
    //卖家
    td = tr.append("td").html(d.seller);
    //金额
    td = tr.append("td").html("¥" + d.amount);
    //状态
    td = tr.append("td").attr("class", "project_progress");
    var div = td.append("div").attr("class", "progress progress_sm");
    var num = (d.state + 1) / StateType.length * 100;
    div.append("div")
        .attr("class", "progress-bar bg-green")
        .attr("role", "progressbar")
        .attr("data-transitiongoal", num)
        .attr("aria-valuenow", num)
        .attr("style","width: "+num+"%");
    td.append("small").html(StateType[d.state]);
    //查看详情
    td = tr.append("td").style("text-align", "center");
    var a = td.append("a")
       // .attr("href", "complaint"+"?"+"id="+d.id)
        .attr("class","btn btn-primary btn-xs")
        .html("查看详情");
    a.on("click", function () {
        window.location = "orderdetails?id="+d.id;
    });
    a.append("i")
        .attr("class","fa fa-pencil");        
}

function drawOrderList()
{
    post("/a2/api/selectOrder", { 'sql': "sql" }, function (data) {
        console.log(data);
        var table = d3.select("#" + "ListTable");
        var tbody = table.select("tbody");
        //var orderList = JSON.parse(ORDERLIST);
        var orderList = ORDERLIST;
        var trs = tbody.selectAll("tr")
            .data(orderList)
            .enter()
            .append("tr");
        trs.each(function (d, i) {
            tr = d3.select(this);
            addOrder(tr, d);
        });
    });
}

function post(URL, PARAMS, f) {
    $.ajax({
        type: "POST",
        url: URL,
        data: JSON.stringify(PARAMS),
        cache: false,
        // async: false,
        contentType: "application/json",
        dataType: "json",
        success: function (data) {
            f(data);
        }
    });
}