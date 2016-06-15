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

var StateType = ["待付款", "待商家确认", "已确认", "交易成功", "交易关闭", "待退款", "已退款", "退款失败"];
var StateTypeH = ["待付款", "待商家确认有房", "已确认有房", "已入住", "交易关闭", "待退款", "已退款", "退款失败","交易成功"];
var StateTypeT = ["待付款", "待出票", "已出票", "已乘机", "交易关闭", "待退款", "已退款", "退款失败","交易成功"];


function post(URL, PARAMS, f) {
    console.log(JSON.stringify(PARAMS));
    $.ajax({
        type: "POST",
        url: URL,
        data: JSON.stringify(PARAMS),
 //       cache: false,
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

function put(URL, PARAMS, f) {
    $.ajax({
        type: "PUT",
        url: URL,
        data: JSON.stringify(PARAMS),
//        cache: false,
        // async: false,
        contentType: "application/json",
        dataType: "json",
        success: function (data) {
            f(data, 0);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            // console.log(XMLHttpRequest);
            // console.log(textStatus);
            // console.log(errorThrown);
            f(0, XMLHttpRequest.status);
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

function payment(order_id, amount)
{
    post("http://121.42.175.1/A1/API/submoney", { 'accountID': userid, 'amount': amount}, function (data, error) {
        data=JSON.parse(data.data).result;
        console.log(data);
        if (data == "NoEnoughMoney") {
            new PNotify({
                title: '操作失败',
                text: '您的余额不足。',
                type: 'error',
                styling: 'bootstrap3'
            });
        } else {
            post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': order_id, 'status': 1 }, function (data, error) {
                if (1==1/*success*/) {
                    new PNotify({
                        title: '操作成功',
                        text: '您已成功付款！',
                        type: 'success',
                        styling: 'bootstrap3'
                    });

                    setTimeout("location.reload();", 3000);
                } else {
                    new PNotify({
                        title: '操作失败',
                        text: '服务器出了点问题，请稍后再试……',
                        type: 'dark',
                        styling: 'bootstrap3'
                    });
                }
            });
        }
    });
}

function confirmorder(order_id) {
    post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': order_id, 'status': 2 }, function (data, error) {
        if (1==1/*success*/) {
            new PNotify({
                title: '操作成功',
                text: '您已成功确认订单！',
                type: 'success',
                styling: 'bootstrap3'
            });

            setTimeout("location.reload();", 3000);
        } else {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        }
    });
}

function receive(orderid, sellerid, amount) {

    // post("http://121.42.175.1/A1/API/addmoney", { 'accountID': sellerid, 'amount': amount}, function (data, error) {
    //     data=JSON.parse(data.data).result;
    //     console.log(data);
    //     if (data != "OK") {
    //         new PNotify({
    //             title: '操作失败',
    //             text: '服务器出了点问题，请稍后再试……',
    //             type: 'dark',
    //             styling: 'bootstrap3'
    //         });
    //     } else {
            post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID':parseInt(orderid), 'status': 3 }, function (data, error) {
                if (1==1/*success*/) {
                    new PNotify({
                        title: '操作成功',
                        text: '您已成功确认消费！',
                        type: 'success',
                    styling: 'bootstrap3'
                    });

                 setTimeout("location.reload();", 3000);
                } else {
                    new PNotify({
                        title: '操作失败',
                        text: '服务器出了点问题，请稍后再试……',
                        type: 'dark',
                        styling: 'bootstrap3'
                    });
                }
            });
    //     }
    // });
}

function refund(orderid) {
    console.log("orderid:"+orderid);
    post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': orderid, 'status': 5 }, function (data, error) {
        if (1==1/*success*/) {
            new PNotify({
                title: '操作成功',
                text: '您已成功申请退款！',
                type: 'success',
                styling: 'bootstrap3'
            });

            setTimeout("location.reload();", 3000);
        } else {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        }
    });
}

function accept(orderid, sellerid, buyerid, amount) {
    // post("http://121.42.175.1/A1/API/submoney", { 'accountID': sellerid, 'amount': amount}, function (data, error) {
    //     data=JSON.parse(data.data).result;
    //     console.log(data);
    //     if (data == "NoEnoughMoney") {
    //         new PNotify({
    //             title: '操作失败',
    //             text: '您的余额不足。',
    //             type: 'error',
    //             styling: 'bootstrap3'
    //         });
    //     } else {
            post("http://121.42.175.1/A1/API/addmoney", { 'accountID': buyerid, 'amount': amount}, function (data, error) {
                data=JSON.parse(data.data).result;
                console.log(data);
                if (data != "OK") {
                    new PNotify({
                        title: '操作失败',
                        text: '服务器出了点问题，请稍后再试……',
                        type: 'dark',
                        styling: 'bootstrap3'
                    });
                } else {
                    post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': orderid, 'status': 6 }, function (data, error) {
                        if (1==1/*success*/) {
                            new PNotify({
                                title: '操作成功',
                                text: '您已成功同意退款！',
                                type: 'success',
                                styling: 'bootstrap3'
                            });

                            setTimeout("location.reload();", 3000);
                        } else {
                            new PNotify({
                                title: '操作失败',
                                text: '服务器出了点问题，请稍后再试……',
                                type: 'dark',
                                styling: 'bootstrap3'
                            });
                        }
                    });
                }
            });
        // }
    // });
}

function closeorder(orderid) {
    post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': orderid, 'status': 4 }, function (data, error) {
        if (1==1/*success*/) {
            new PNotify({
                title: '操作成功',
                text: '您已成功取消订单！',
                type: 'success',
                styling: 'bootstrap3'
            });

            setTimeout("location.reload();", 3000);
        } else {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        }
    });
}

function closeorderandrefund(orderid, buyerid, amount) {
post("http://121.42.175.1/A1/API/addmoney", { 'accountID': buyerid, 'amount': amount}, function (data, error) {
        data=JSON.parse(data.data).result;
        console.log(data);
        if (data != "OK") {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        } else {
            post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID':parseInt(orderid), 'status': 4 }, function (data, error) {
                if (1==1/*success*/) {
                    new PNotify({
                        title: '操作成功',
                        text: '您已成功取消订单，已付款项已退款至您的账户！',
                        type: 'success',
                    styling: 'bootstrap3'
                    });

                 setTimeout("location.reload();", 3000);
                } else {
                    new PNotify({
                        title: '操作失败',
                        text: '服务器出了点问题，请稍后再试……',
                        type: 'dark',
                        styling: 'bootstrap3'
                    });
                }
            });
        }
    });
}

function reject(orderid) {
    post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID': orderid, 'status': 7 }, function (data, error) {
        if (1==1/*success*/) {
            new PNotify({
                title: '操作成功',
                text: '您已成功拒绝退款！',
                type: 'success',
                styling: 'bootstrap3'
            });

            setTimeout("location.reload();", 3000);
        } else {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        }
    });
}

function finish(orderid, sellerid, amount) {
    post("http://121.42.175.1/A1/API/addmoney", { 'accountID': sellerid, 'amount': amount}, function (data, error) {
        data=JSON.parse(data.data).result;
        console.log(data);
        if (data != "OK") {
            new PNotify({
                title: '操作失败',
                text: '服务器出了点问题，请稍后再试……',
                type: 'dark',
                styling: 'bootstrap3'
            });
        } else {
            post("http://121.42.175.1/a2/api/updateorderstate", { 'orderID':parseInt(orderid), 'status': 8 }, function (data, error) {
                if (1==1/*success*/) {
                    new PNotify({
                        title: '操作成功',
                        text: '您已成功完成交易！',
                        type: 'success',
                        styling: 'bootstrap3'
                    });

                 setTimeout("location.reload();", 3000);
                } else {
                    new PNotify({
                        title: '操作失败',
                        text: '服务器出了点问题，请稍后再试……',
                        type: 'dark',
                        styling: 'bootstrap3'
                    });
                }
            });
        }
    });
}

function drawInfo(data, user_id)
{
    var isBuyer;
    console.log(data);
    isBuyer = 1 - userType;
    var accountName;
    if (isBuyer==1) {
        post("http://121.42.175.1/A1/API/userInfoAPI", {  'accountID': data.seller }, function (data1, error) {
              data1 = JSON.parse(data1.data);
              accountName = data1.AccountName;
              console.log("sellername "+accountName);
              // d3.selectAll(".username").html(accountName);
              d3.select("#sellerName").html(accountName);
          });
       // d3.select("#sellerName").html(data.seller);
    } else {
        post("http://121.42.175.1/A1/API/userInfoAPI", {  'accountID': data.buyer }, function (data1, error) {
              data1 = JSON.parse(data1.data);
              accountName = data1.AccountName;
              // d3.selectAll(".username").html(accountName);
              d3.select("#sellerName").html(accountName);
          });
       // d3.select("#sellerName").html(data.buyer);
    }

    d3.select("#orderdate").html(data.orderTime);
    console.log("test~" + JSON.parse(data.orderItems)[0].id);
    if (JSON.parse(data.orderItems)[0].id[0]=="H") {
        d3.select("#orderstate").html(StateTypeH[data.orderStatus]);
    } else {
        d3.select("#orderstate").html(StateTypeT[data.orderStatus]);
    }
    d3.select("#orderamount").html(data.orderAmount+"元");
    if (data.orderStatus==0) {
        //需要判断是不是买家
        if (isBuyer == 1) {
            var div = d3.select("#order_info");
            var br = div.append("br");
            var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "payment(orderid, "+data.orderAmount+");").html("付款");
            a = div.append("a").attr("class", "btn btn-success").attr("onclick", "closeorder(orderid)").html("取消订单");
        }
    }

    if (data.orderStatus==1) {
        //需要判断是不是卖家
        if (isBuyer == 0) {
            var div = d3.select("#order_info");
            var br = div.append("br");
            var a;
            if (JSON.parse(data.orderItems)[0].id[0]=="H") {
                a = div.append("a").attr("class", "btn btn-success").attr("onclick", "confirmorder(orderid);").html("确认有房");
            } else {
                a = div.append("a").attr("class", "btn btn-success").attr("onclick", "confirmorder(orderid);").html("确认出票");
            }
            
            a = div.append("a").attr("class", "btn btn-success").attr("onclick", "closeorderandrefund(orderid, "+data.buyer+", "+data.orderAmount+");").html("取消订单");
        } else {
            var div = d3.select("#order_info");
            var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "refund(orderid);").html("申请退款");
        }
    }
    console.log("test");
    if (data.orderStatus==2) {
        //需要判断是不是卖家
        console.log("test");
        if (isBuyer == 0) {
            var div = d3.select("#order_info");
            var a;
            console.log("test");
            if (JSON.parse(data.orderItems)[0].id[0]=="H") {
                console.log("test");
                a = div.append("a").attr("id", "confirmOK").attr("class", "btn btn-success").html("确认入住");
            } else {
                // d3.select("#confirm_Order").style("display", "block");
                a = div.append("a").attr("id", "confirmOK").attr("class", "btn btn-success").html("确认乘机");
            }
            // d3.select("#ordercode").html("验证码："+"1234567890");
        //    var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "receive(orderid, "+data.seller+", "+data.orderAmount+");").html("确认收货");
        }
        else{
            d3.select("#ordercode").html("验证码："+data.captcha);
        }

        d3.select("#confirmButton").on("click", function() {
            var ordercodeVar = document.getElementById("codeText");
            ordercodeVar = ordercodeVar.value;
            console.log(ordercodeVar);
            if (data.captcha!=ordercodeVar) {
                new PNotify({
                    title: '操作失败',
                    text: '验证码错误，确认消费失败。',
                    type: 'error',
                    styling: 'bootstrap3'
            });
            } else {
                receive(orderid, data.seller, data.orderAmount);
            }
        });
        //attr("onclick", "receive(orderid, "+data.seller+", "+data.orderAmount+", "+ordercodeVar+");");
        d3.select("#confirmOK").on("click", function () {
                  d3.select("#confirm_Order").style("display", "block");
                  // drawOrderList(userID, 0);
              });
          
    }

    if (data.orderStatus==3) {
        //需要判断是不是买家
        if (isBuyer == 1) {
            var div = d3.select("#order_info");
            var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "refund(orderid);").html("申请退款");
            a = div.append("a").attr("class", "btn btn-success").attr("onclick", "finish(orderid, "+data.seller+", "+data.orderAmount+");").html("完成交易");
        }
    }

    if (data.orderStatus==5) {
        //需要判断是不是卖家
        if (isBuyer == 0) {
            var div = d3.select("#order_info");
            var br = div.append("br");
            var a = div.append("a").attr("class", "btn btn-success").attr("onclick", "accept(orderid, "+data.seller+", "+data.buyer+", "+data.orderAmount+");").html("同意退款");
            a = div.append("a").attr("class", "btn btn-success").attr("onclick", "reject(orderid);").html("拒绝退款");
        }

    }

    if (data.orderStatus==8) {
        //需要判断是不是买家
        if (isBuyer == 1 && JSON.parse(data.orderItems)[0].id[0] == "H") {
            var div = d3.select("#order_info");
        var a = div.append("a").attr("class", "btn btn-success").attr("id", "to_Comment").html("评价")
            .on("click", function () {
                console.log("click");
                get("http://121.42.175.1/a3/getdetail", { 'ID': JSON.parse(data.orderItems)[0].id}, function (itemData, error) {
                    console.log(itemData);
                    window.location = "comment?Hotel_ID=" + itemData.Hotel_ID + "&HotelName=" + itemData.Hotel_Name + "&OrderPrice=2016&OrderDate=" + data.orderAmount;   //TODO
                });
            });
        }
    }

    //交易关闭、已退款和退款失败没有额外按钮

    var div = d3.select("#order_info");
    if (1==1) {//如果没有在投诉中
        var a = div.append("a").attr("class", "btn btn-success").attr("id", "to_Comp").html("投诉订单")
            .on("click", function () {
                console.log("click");
                window.location = "complaint?orderID=" + orderid;
            });
    } else {
        var li = div.append("li").html("投诉中：此处显示投诉信息，信息可能很长，所以测试一下换行的效果好不好看");
    }
}

function drawGoods(alldata, data) {
    console.log(data);
    var table = d3.select("#contentTable");
    var tbody = table.select("tbody");
    var trs = tbody.selectAll("tr")
               .data(data)
               .enter()
               .append("tr");
    trs.each(function (d, i) {
        tr = d3.select(this);
        get("http://121.42.175.1/a3/getdetail", { 'ID': d.id }, function (itemData, error) {
            console.log(itemData);
            console.log(itemData.File_Pos);
            var td;
            if (d.id[0]=="T") {
                tr.append("td").append("img").attr("src", "http://121.42.175.1:5003/avatar/flight.png")
                .attr("width", "100px")
                .attr("height","100px");
                td = tr.append("td").html(itemData.Flight_Company);//d.title);
            } else {
                tr.append("td").append("img").attr("src", "http://121.42.175.1:5003/"+itemData.File_Pos)
                .attr("width", "100px")
                .attr("height","100px");
                td = tr.append("td").html(itemData.Hotel_Name);//d.title);
            }

            td = tr.append("td").html(alldata.orderAmount+"元");//d.amount/d.quantity);
            td = tr.append("td").attr("class", "hidden-phone").html("1");//d.quantity);
            td = tr.append("td").attr("class", "vertical-align-mid").html(alldata.orderAmount+"元");//d.amount);
        });

        // tr.append("td").append("img").attr("src", "http://img2.imgtn.bdimg.com/it/u=355596720,3737965610&fm=206&gp=0.jpg")
        //     .attr("width", "50px")
        //     .attr("height","50px");

    });
}

function drawOrderDetails(order_id, user_id)
{
    console.log(order_id);
    d3.select("#order_ID").html("订单号："+order_id);
    get("http://121.42.175.1/a2/api/getorderdetial", { 'orderID': order_id }, function (data, error) {
        console.log("getorderdetial");
        console.log(data);
        // data = JSON.parse(data);
        drawInfo(data, user_id);
        console.log(JSON.parse(data.orderItems));
        drawGoods(data, JSON.parse(data.orderItems));
    });
}