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

var StateType = ["待付款", "待商家确认房间/待出票", "房间已确认/已出票", "已入住/已乘机", "交易关闭", "待退款", "已退款", "退款失败"];
var statusNo = {
    '所有状态':-1,
    '待付款':0,
    '待商家确认房间/待出票': 1,
    '房间已确认/已出票': 2,
    '已入住/已乘机': 3,
    '待退款':5,
    '已退款':6,
    '退款失败':7
};
var timeNo = {
    '所有时间':-1,
    '一日内':0,
    '一周内':1,
    '一月内':2,
    '一年内':3
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
            f(data,0);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            f(0, XMLHttpRequest.status);
        }
    });
}

function get(URL, PARAMS, f) {
    URL += '?';
    var flag = false;
    for (var p in PARAMS)
    {
        if (flag) URL += '&';
        URL += p + '=' + PARAMS[p];
        flag = true;
    }
    console.log(URL);
    $.ajax({
        type: "GET",
        url: URL,
        // data: JSON.stringify(PARAMS),
        cache: false,
        // async: false,
        contentType: "application/json",
        dataType: "json",
        success: function (data) {
            f(data,0);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            f(0, XMLHttpRequest.status);
        }
    });
}

function addOrder(tr,orderID)
{
    var oppoType = ['seller','buyer'];
    get("http://121.42.175.1/a2/api/getorderdetial", { 'orderID': orderID }, function (data) {
        tr.append("td").html("");
        //订单编号
        var td = tr.append("td");
        td.append("a").html(orderID);
        td.append("br");
        td.append("small").html(data.orderTime);
        //商品
        items = JSON.parse(data.orderItems);
        console.log(items);
        td = tr.append("td");
        var ul = td.append("ul").attr("class", "list-inline").attr("id","UL"+orderID);
        var lis = ul.selectAll("li")
            .data(items)
            .enter()
            .append("li");
        lis.each(function (d, i) {
            var li = d3.select(this);
            get("http://121.42.175.1/a3/getdetail", { 'ID': d.id }, function (itemData, error) {
                console.log(itemData);
                console.log(itemData.File_Pos);
                //d3.select("#" + "O" + orderID)
                //var li = d3.select("#"+"O"+)
                li.append("img")
                    .attr("src", itemData.File_Pos)
                    .style("width", "50px")
                    .style("height", "50px");
                // data = JSON.parse(data.data);
            });
        });
       
        //data.imgsrc = ['http://img2.imgtn.bdimg.com/it/u=355596720,3737965610&fm=206&gp=0.jpg', 'http://img2.imgtn.bdimg.com/it/u=355596720,3737965610&fm=206&gp=0.jpg'];
        //for (var p in data.imgsrc) {
        //    ul.append("li").append("img")
        //        .attr("src", data.imgsrc[p])
        //        .style("width", "50px")
        //        .style("height", "50px");
        //}
        //卖家/买家
        td = tr.append("td").attr('id', 'td' + orderID);
        //'accountID': data[oppoType[userType]] 
        post("http://121.42.175.1/A1/API/userInfoAPI", {  'accountID': 123 }, function (data, error){ 
            data = JSON.parse(data.data);
            var name = data.AccountName;
            td = d3.select("#td" + orderID)
                .html(name);
        });
        //金额
        td = tr.append("td").html("¥" + data.orderAmount);
        //状态
        td = tr.append("td").attr("class", "project_progress");
        var div = td.append("div").attr("class", "progress progress_sm");
        var normal;
        var progress;
        if (data.orderStatus <= 4) {
            normal = true;
            progress = (data.orderStatus + 1) / 4 * 100;
            if (data.status > 2)
                progress = 100;
        }
        else
        {
            normal = false;
            if (data.orderStatus > 5)
                progress = 100;
            else
                progress = 50;
        }
       // progress = 50;
           div.append("div")
            .attr("class", function () {
                var c = "progress-bar"
                if (data.orderStatus <= 4)
                    c += " bg-blue";
                else
                    c += " bg-red";
                return c;
            })
            .attr("role", "progressbar")
            .attr("data-transitiongoal", progress)
            .attr("aria-valuenow", progress)
            .attr("style", "width: " + progress + "%");
        td.append("small").html(StateType[data.orderStatus]);
        //查看详情
        td = tr.append("td").style("text-align", "center");
        var a = td.append("a")
            .datum(orderID)
           // .attr("href", "complaint"+"?"+"id="+d.id)
            .attr("class", "btn btn-primary btn-xs")
            .html("查看详情");
        a.on("click", function (d) {
            window.location = "orderdetails?orderID="+d;
        });
        a.append("i")
            .attr("class", "fa fa-pencil");
    });
    return;
}

function drawOrderList(userID,sort)
{
    var selTime = d3.select("#selectTime").property("value");
    selTime = timeNo[selTime];
    var selStatus = d3.select("#selectStatus").property("value");
    selStatus = statusNo[selStatus];
    console.log(selStatus);
    var postObj = new Object();
    postObj['userID'] = userID;
    postObj['date'] = selTime;
    postObj['status'] = selStatus;
    postObj['sort'] = sort;
    // console.log("sort: " + sort);
    console.log(postObj);
    get("http://121.42.175.1/a2/api/getorder",postObj, function (data) {
        console.log(data);
        //console.log("post: "+data);
        orderList = new Array();
        data = data['orderIdList'];
        for (var p in data)
        {
            orderList.push(data[p].orderID);
        }
        var table = d3.select("#" + "ListTable");
        var tbody = table.select("tbody");
        tbody.selectAll("tr").remove();
        var trs = tbody.selectAll("tr")
            .data(orderList)
            .enter()
            .append("tr");
        trs.each(function (d, i) {
            tr = d3.select(this);
            addOrder(tr,d);
        });
    });
    return;


    post("/a2/api/selectOrder", { 'sql': "sql" }, function (data) {
        //data = JSON.parse(data);
        console.log(data);
        var table = d3.select("#" + "ListTable");
        var tbody = table.select("tbody");
        //var orderList = JSON.parse(ORDERLIST);
        var orderList = JSON.parse(data);
        console.log(orderList);
        var trs = tbody.selectAll("tr")
            .data(orderList)
            .enter()
            .append("tr");
        trs.each(function (d, i) {
            tr = d3.select(this);
            addOrder(tr, d,i);
        });
    });
}

function search()
{
    var searchID = document.getElementById('searchText').value;
    if (!searchID) {
        drawOrderList(userID, 0);
        return;
    }
    var table = d3.select("#" + "ListTable");
    var tbody = table.select("tbody");
    tbody.selectAll("tr").remove();
    get("http://121.42.175.1/a2/api/getorderdetial", { 'orderID': searchID }, function (data, error) {
        if (error || data.buyer != userID) {
            d3.select("#notifyDIV").style("display", "block");
            setTimeout(function () {
                d3.select("#notifyDIV").style("display", "none");
            }, 800);
            return;
        }
        var tr = tbody.append("tr").datum(searchID);
        addOrder(tr, searchID);
    });
}

function EnterPress(e) { //传入 event
    var e = e || window.event;
    if (e.keyCode == 13) {
        search();
    }
}

