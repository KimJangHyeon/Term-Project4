var i_day = 0;
var i_room = 0;

// 0 오늘 1 내일 2 모래
var arr_day0_room0 = [
    "1","","","","","","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];

var arr_day1_room0 = [
    "","2","","","","","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];

var arr_day2_room0 = [
    "","","3","","","","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];

var arr_day0_room1 = [
    "","","","4","","","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];

var arr_day1_room1 = [
    "","","","","5","","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];

var arr_day2_room1 = [
    "","","","","","6","",
    "","","","","","","",
    "","","","","","","",
    "","","","","","",""];


var move = function(delta) {
    i_day += delta;
    if (i_day < 0 || i_day > 2) {
        i_day -= delta;
        alert("거긴 못가!");
    } else {
        if (i_day === 0) {
            if (i_room === 0) {
                show_graph(arr_day0_room0);
            } else if (i_room === 1) {
                show_graph(arr_day0_room1);
            }
        } else if (i_day === 1) {
            if (i_room === 0) {
                show_graph(arr_day1_room0);
            } else if (i_room === 1) {
                show_graph(arr_day1_room1);
            }
        } else if (i_day === 2) {
            if (i_room === 0) {
                show_graph(arr_day2_room0);
            } else if (i_room === 1) {
                show_graph(arr_day2_room1);
            }
        }
    }
};

var show_graph = function(arr) {
    var graph_innerHTML = "";
    graph_innerHTML += "<ul class=\"chart-skills\">";

    for (var i = 0; i < 28; i++) {
        if (arr[i] === "") {
            graph_innerHTML +=
                "<li title=\""
                + ((i/2)+8) + ":" + (i%2)*30 + " ~ "
                + (((i+1)/2)+8) + ":" + ((i+1)%2)*30 + "\""
                + "><span></span></li>";
            //style="border-color: #00ff00"
        }
    }

    document.getElementById("content_graph").innerHTML = graph_innerHTML;
};