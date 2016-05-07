//测试数据
var orderList = [
{
    id:"SE000010325",
    time: "2016.3.24",
    user: "ZaneXiao",
    amount: 66.2,
    state: "NotDel",
    imgsrc:"1.jpg"
},
{
    id: "SE000010510",
    time: "2016.3.22",
    user: "EowinYe",
    amount: 99.8,
    state: "Delivery",
    imgsrc:"2.jpg"
},
{
    id: "SE000010296",
    time: "2016.3.21",
    user: "ABC",
    amount: 12.5,
    state: "Success",
    imgsrc: "3.jpg"
}
];

var ORDERS = {
    "SE000010325": {
        id: "SE000010325",
        time: "2016.3.24",
        user:"ZaneXiao",
        state: "NotDel",
        amount: 664.8,
        content: [
            {
                title: "云恋酒店（不含早）",
                quantity:2,
                amount: 576.0,
                imgsrc:"1.jpg"
            },
            {
                title: "会员增值业务",
                quantity: 1,
                amount: 88.8,
                imgsrc:"3.jpg"
            }
        ],
        flow: [
            {
                time: "2016.3.21 14:11",
                summary:"买家zyy已付款"
            },
            {
                time: "2016.3.22 00:03",
                summary: "卖家YunlianHotel确认订单"
            },
            {
            time: "2016.3.22 00:04",
                summary: "卖家YunlianHotel确认发货"
            },
            {
                time: "2016.3.25 19:52",
                summary: "买家zyy确认收货,交易完成"
            }
        ]
    }
};

var COMPLAINTS = {
    "SE000010325": {
        id: "SE000010325",

    }
};

//测试数据-结束

var divID = "OrderDiv";
var divTop= 60;
var StateType={
    "NotPay":"待付款",
    "NotDel":"待发货",
    "Delivery":"已发货",
    "Success":"交易成功",
    "NotRef":"待退款",
    "Refund":"已退款",
    "Compl":"投诉中"
};

function drawOrderList()
{
    var div = d3.select("#" + divID);
    var group = div.selectAll("g");
    group.remove();
    group = div.append("g")
        .attr("id", "ListGroup");
    var BackHeight = 200;
    var interval = 50;
    var orders = group.selectAll("div")
        .data(orderList) //绑定订单数据
        .enter()
        .append("div")
        .attr("class", "OrderBack")
        .style("height", BackHeight+"px")
        .style("top", function (d, i) {
            return divTop + interval * (i) + BackHeight * i+"px";
        })
        .on("click", function (d, i) {
            d3.select("#ListGroup")
                .transition().duration(200)
                .style("opacity", 0);
            drawOrder(d.id);
        });
    orders.each(function(d,i){
        var order = d3.select(this);
        var TitleHeight = 40;
        //标题
        var title = order.append("div")
            .attr("class", "OrderTitle")
            .style("height", TitleHeight + "px")
            .style("top","5px");
        var titleTable = title.append("table")
            .style("table-layout", "fixed")
            .style("position", "absolute")
            .style("top", "48%")
            .style("left","1.5%")
            .style("width","97%");
        var titTr = titleTable.append("tbody").append("tr");
        titTr.append("td")
            .style("text-align","left")
            .html("订单编号: "+d.id);
        titTr.append("td")
            .style("text-align","right")
            .html(d.time);
        //订单信息
        var infTable = order.append("table")
           .style("table-layout", "fixed")
           .style("position", "absolute")
           .style("top", "25%")
           .style("left", "3%")
           .style("width", "94%")
           .style("height","75%");
        var infTr = infTable.append("tbody").append("tr")
            .style("text-align","center");
        infTr.append("td")
            .append("img")
            .attr("src", d.imgsrc)
            .attr("width","96%");
        infTr.append("td")
            .html(d.user);
        infTr.append("td")
            .html("¥" + d.amount);
        infTr.append("td")
            .html(StateType[d.state]);
    });
}

function drawOrder(orderID)
{
    orderID = "SE000010325";//测试
    var order = ORDERS[orderID];//取得订单数据
    var div = d3.select("#" + divID);
    var group = div.append("g")
            .attr("id", "OrderGroup")
            .style("opacity",0);
    group.transition().duration(4000)
            .ease("elastic")
            .style("opacity", 1);
    var titleHeight = 40;
    var termHeight = 110;
    var titleHeight = 40;
    var stateHeight = 80;
    var contentHeight = (order.content.length + 1) * termHeight + titleHeight;
    var cplHeight = 80;
    var panel = group.append("div")
       .attr("class", "OrderBack")
       .style("position", "absolute")
       .style("top", divTop + "px")
       .style("height",stateHeight + contentHeight+cplHeight+"px");
    var stateDiv = panel.append("div")
        .style("position", "relative")
        .style("height", stateHeight + "px");
    var contentDiv = panel.append("div")
            .style("height", contentHeight + "px")
            .style("position", "relative")
            .style("top", stateHeight + "px");
    var cplDiv = panel.append("div")
           .style("height", cplHeight+"px")
           .style("position", "relative")
           .style("top",  40 + "px");

    //stateDiv
    var title = stateDiv.append("div")
           .attr("class", "OrderTitle")
           .style("height", titleHeight + "px")
           .style("top", "5px");
    var titleTable = title.append("div").append("table")
            .style("table-layout", "fixed")
            .style("position", "absolute")
            .style("top", "48%")
            .style("left", "1.5%")
            .style("width", "97%");
    var titTr = titleTable.append("tbody").append("tr");
    titTr.append("td")
        .style("text-align", "left")
        .html("订单编号: " + order.id);
    titTr.append("td")
        .style("text-align", "right")
        .html(order.time);
    var stateInfoTable = stateDiv.append("table")
          .style("table-layout", "fixed")
          .style("position", "absolute")
          .style("top", titleHeight+15+"px")
          .style("left", "1.5%")
          .style("width", "97%")
          .style("text-align","left");
    var sitbody = stateInfoTable.append("tbody");
    sitbody.append("tr").append("td")
        .html("卖家: " + order.user);
    sitbody.append("tr").append("td")
        .html("交易状态: " + StateType[order.state]);
    sitbody.append("tr").append("td")
        .html("支付金额: ¥" + order.amount);

    //contentDiv
    var content = contentDiv.append("div")
          .attr("class", "OrderTitle")
          .style("height", titleHeight + "px")
          .style("top", "5px")
          .style("border-radius", "0px");
    var ctTable = content.append("div").append("table")
            .style("table-layout", "fixed")
            .style("position", "absolute")
            .style("top", "48%")
            .style("left", "1.5%")
            .style("width", "97%");
    var ctTr = ctTable.append("tbody").append("tr");
    ctTr.append("td")
        .style("text-align", "left")
        .html("商品内容");
    ctTr.append("td")
        .style("text-align", "right")
        .html("数量");
    ctTr.append("td")
        .style("text-align", "right")
        .html("总价");

    var cntInfoTable = contentDiv.append("table")
          .style("table-layout", "fixed")
          .style("position", "absolute")
          .style("top", titleHeight+8+"px")
          .style("left", "1.5%")
          .style("width", "97%")
          .style("height",order.content.length*termHeight+"px")
          .style("text-align", "center");

    var cntbody = cntInfoTable.append("tbody");
    var cnttrs = cntbody.selectAll("tr")
        .data(order.content)
        .enter()
        .append("tr");
    cnttrs.each(function (d, i) {
        var tr = d3.select(this);
        tr.append("td")
            .append("img")
            .attr("src", d.imgsrc)
            .attr("width", "96%");;
        tr.append("td")
            .html(d.title);
        tr.append("td")
            .html(d.quantity);
        tr.append("td")
            .style("text-align", "right")
            .html("¥" + d.amount);
    });
    var ctr = cntbody.append("tr");
    ctr.append("td");
    ctr.append("td");
    ctr.append("td");
    ctr.append("td")
            .style("text-align", "right")
            .html("总金额&nbsp&nbsp&nbsp¥" + order.amount);

    //cplDiv
    cplDiv.style("font-size","85%");
    cplDiv.append("nobr")
        .html("&nbsp&nbsp交易出现问题？");
    cplDiv.append("nobr")
        .style("color", "blue")
        .html("&nbsp&nbsp申请退款？");
    cplDiv.append("nobr")
        .style("color", "blue")
        .html("&nbsp&nbsp投诉该订单？")
        .on("click", function () {
            group.transition().duration(200)
                .style("opacity", 0)
                .remove();
            drawComplaint(orderID);
        });
}

function drawComplaint(orderID)
{
    orderID = "SE000010325";//测试
    var order = ORDERS[orderID];//取得订单信息
    var div = d3.select("#" + divID);
    var group = div.append("g")
            .attr("id", "ComplaintGroup")
            .style("opacity", 0);
    group.transition().duration(4000)
            .ease("elastic")
            .style("opacity", 1);
    var titleHeight = 40;
    var termHeight = 32;
    var titleHeight = 40;
    var orderHeight = (order.flow.length) * termHeight + titleHeight;
    var cplHeight = 350;
    var panel = group.append("div")
       .attr("class", "OrderBack")
       .style("position", "absolute")
       .style("top", divTop + "px")
       .style("height", orderHeight + cplHeight + "px");
    var orderDiv = panel.append("div")
        .style("position", "relative")
        .style("height", orderHeight + "px");
    var cplDiv = panel.append("div")
            .style("height", cplHeight + "px")
            .style("position", "relative")
            .style("top", 0 + "px");

    //orderDiv
    var title = orderDiv.append("div")
           .attr("class", "OrderTitle")
           .style("height", titleHeight + "px")
           .style("top", "5px");
    var titleTable = title.append("div").append("table")
            .style("table-layout", "fixed")
            .style("position", "absolute")
            .style("top", "48%")
            .style("left", "1.5%")
            .style("width", "97%");
    var titTr = titleTable.append("tbody").append("tr");
    titTr.append("td")
        .style("text-align", "left")
        .html("投诉订单号: " + order.id);
    var orderTable = orderDiv.append("table")
         // .style("table-layout", "fixed")
          .style("position", "absolute")
          .style("top", titleHeight + 15 + "px")
          .style("left", "1.5%")
          //.style("width", "97%")
          .style("border-spacing", "0px")
          .style("text-align", "left")
          .style("font-size","80%");
    var orderbody = orderTable.append("tbody");
    var trs = orderbody.selectAll("tr")
        .data(order.flow)
        .enter()
        .append("tr");
    trs.each(function(d,i)
    {
        var tr = d3.select(this);
        tr.append("td")
            .append("svg")
            .style("height", "10px")
            .style("width", "25px")
            .append("circle")
            .attr("cx", "10px")
            .attr("cy","5px")
            .attr("r", "4px")
            .style("fill","orange")
        tr.append("td")
           .html(d.time+" "+d.summary);
    });

    //cplDiv
    var cplTitle = cplDiv.append("div")
          .attr("class", "OrderTitle")
          .style("height", titleHeight + "px")
          .style("top", "5px")
          .style("border-radius", "0px");
    var cplTable = cplTitle.append("div").append("table")
            .style("table-layout", "fixed")
            .style("position", "absolute")
            .style("top", "48%")
            .style("left", "1.5%")
            .style("width", "97%");
    cplTable.append("tbody").append("tr").append("td")
        .html("投诉理由");
    var textField = cplDiv.append("textarea")
        .attr("id","textfield")
        .style("position", "absolute")
        .style("top", titleHeight + 30 + "px")
        .style("left", "8%")
        .style("width", "84%")
        .style("height", "55%")
        .style("resize","none")
        .html("请详细说明投诉理由...");
    var button = cplDiv.append("button")
        .style("position", "absolute")
        .style("margin","0 auto")
        .style("top", "82%")
        .style("left", "45%")
        .style("width", "10%")
        .style("height", "30px")
        .html("提交")
        .on("click", function () {
            console.log(document.getElementById('textfield').value);
        });
}
