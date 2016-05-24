var ORDERS = '{\
        "id": "SE000010325",\
        "time": "2016.3.24",\
        "user":"ZaneXiao",\
        "state": "1",\
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
                "imgsrc": "http://www.cysz6.com/upload/hotel/1305/29/28664d284e439a97cbd622d2be6d35d9.jpg"\
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

var StateType = ["待付款", "待商家确认", "已确认", "交易成功", "待退款", "已退款", "退款失败"];

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

function get(URL, PARAMS, f) {
    for (var p in PARAMS)
    {
        URL += '?' + p + '=' + PARAMS[p];
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
            f(data);
        }
    });
}

function addGood(tbody,tr)
{
    tbody.append("tr").html("");
    //订单编号
    // var td = tr.append("td");
    // td.append("a").html(d.id);
    // td.append("br");
    // td.append("small").html(d.time);
    // //商品
    // td = tr.append("td");
    // var ul = td.append("ul").attr("class", "list-inline");
    // for (var p in d.imgsrc)
    // {
    //     ul.append("li").append("img")
    //         .attr("src", d.imgsrc[p])
    //         .style("width", "50px")
    //         .style("height", "50px");
    // }
    // //卖家
    // td = tr.append("td").html(d.seller);
    // //金额
    // td = tr.append("td").html("¥" + d.amount);
    // //状态
    // td = tr.append("td").attr("class", "project_progress");
    // var div = td.append("div").attr("class", "progress progress_sm");
    // var num = (d.state + 1) / StateType.length * 100;
    // div.append("div")
    //     .attr("class", "progress-bar bg-green")
    //     .attr("role", "progressbar")
    //     .attr("data-transitiongoal", num)
    //     .attr("aria-valuenow", num)
    //     .attr("style","width: "+num+"%");
    // td.append("small").html(StateType[d.state]);
    // //查看详情
    // td = tr.append("td").style("text-align", "center");
    // var a = td.append("a")
    //    // .attr("href", "complaint"+"?"+"id="+d.id)
    //     .attr("class","btn btn-primary btn-xs")
    //     .html("查看详情");
    // a.on("click", function () {
    //     window.location = "orderdetails?id="+d.id;
    // });
    // a.append("i")
    //     .attr("class","fa fa-pencil");        

}

function drawInfo(data)
{
    console.log(data);
    d3.select("#sellerName").html(data.seller);
    d3.select("#orderdate").html(data.orderTime);
    d3.select("#orderstate").html(StateType[data.orderStatus]);
    d3.select("#orderamount").html(data.orderAmount);
    if (data.orderStatus==0) {
        //需要判断是不是买家
        var div = d3.select("#order_info");
        var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功付款！',type: 'success',styling: 'bootstrap3'});").html("付款");
    }

    if (data.orderStatus==1) {
        //需要判断是不是卖家
        var div = d3.select("#order_info");
        var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功确认订单！',type: 'success',styling: 'bootstrap3'});").html("确认订单");
    }

    if (data.orderStatus==2) {
        //需要判断是不是买家
        var div = d3.select("#order_info");
        var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功确认收货！',type: 'success',styling: 'bootstrap3'});").html("确认收货");
    }

    if (data.orderStatus==3) {
        //需要判断是不是买家
        var div = d3.select("#order_info");
        var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功申请退款！',type: 'success',styling: 'bootstrap3'});").html("申请退款");
    }

    if (data.orderStatus==4) {
        //需要判断是不是卖家
        var div = d3.select("#order_info");
        var br = div.append("br");
        var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功同意退款！',type: 'success',styling: 'bootstrap3'});").html("同意退款");
        a = div.append("a").attr("class", "btn btn-success").attr("onclick", "new PNotify({title: '操作成功',text: '您已成功拒绝退款！',type: 'success',styling: 'bootstrap3'});").html("拒绝退款");
    }

    //已退款和退款失败没有额外按钮
}

function drawGoods(data) {
    console.log(data);
    var table = d3.select("#contentTable");
    var tbody = table.select("tbody");
    var trs = tbody.selectAll("tr")
               .data(data)
               .enter()
               .append("tr");
    trs.each(function (d, i) {
        tr = d3.select(this);
        //此处应该接A3的api
        tr.append("td").append("img").attr("src", d.imgsrc)
            .attr("width", "50px")
            .attr("height","50px");
        var td = tr.append("td").html("此处显示商品名");//d.title);
        td = tr.append("td").html("此处显示单价");//d.amount/d.quantity);
        td = tr.append("td").attr("class", "hidden-phone").html("此处显示数量");//d.quantity);
        td = tr.append("td").attr("class", "vertical-align-mid").html("此处显示总价");//d.amount);
    });
}

function drawOrderDetails(order_id)
{
    console.log(order_id);
    d3.select("#order_ID").html("订单号："+order_id);
    get("http://121.42.175.1/a2/api/getorderdetial", { 'orderID': 1 }, function (data) {
        console.log(data);
        // data = JSON.parse(data);
        drawInfo(data);
        drawGoods(JSON.parse(data.orderItems).items);
    });
}