var StateType = ["待付款", "待商家确认房间/待出票", "房间已确认/已出票", "已入住/已乘机", "交易关闭", "待退款", "已退款", "退款失败","交易成功"];
var statusNo = {
    '所有状态':-1,
    '待付款':0,
    '待商家确认房间/待出票': 1,
    '房间已确认/已出票': 2,
    '已入住/已乘机': 3,
    '待退款':5,
    '已退款':6,
    '退款失败': 7,
    '交易成功':8
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
        td = tr.append("td");
        var ul = td.append("ul").attr("class", "list-inline").attr("id","UL"+orderID);
        var lis = ul.selectAll("li")
            .data(items)
            .enter()
            .append("li");
        lis.each(function (d, i) {
            var li = d3.select(this);
            console.log(d.id[0]);
            if (d.id[0] == "T")
            {
               li.append("img")
                .attr("src", "http://121.42.175.1:5003/avatar/flight.png")
                .style("width", "50px")
                .style("height", "50px");
            }
            else
            get("http://121.42.175.1/a3/getdetail", { 'ID': d.id }, function (itemData, error) {
                li.append("img")
                    .attr("src","http://121.42.175.1:5003/"+itemData.File_Pos)
                    .style("width", "50px")
                    .style("height", "50px");
            });
        });
       
        
        //卖家/买家
        td = tr.append("td").attr('id', 'td' + orderID);
        var checkID = data.seller;
        if (userType == 1)
            checkID = data.buyer;
        post("http://121.42.175.1/A1/API/userInfoAPI", {  'accountID': checkID }, function (data, error){ 
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
        if (data.orderStatus <= 4 || data.orderStatus == 8) {
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
    var postObj = new Object();
    postObj['userID'] = userID;
    postObj['date'] = selTime;
    postObj['status'] = selStatus;
    postObj['sort'] = sort;
    get("http://121.42.175.1/a2/api/getorder",postObj, function (data) {
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

