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
    
}

function drawOrderDetails(order_id)
{
    post("/a2/api/selectOrder", { 'sql': "sql" }, function (data) {
        data = JSON.parse(ORDERS);
        drawInfo(data);
        drawGoods(data.content);
    });
}