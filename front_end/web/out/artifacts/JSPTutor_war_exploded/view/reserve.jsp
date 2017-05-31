<%@ page import="component.Header" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Iterator" %>
<%@ page import="java.util.Collection" %>
<%@ page import="java.util.ListIterator" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            width: 100%;
            height: 100%;
            margin: 0;
        }
    </style>

    <link rel="stylesheet" type="text/css" href="../stylesheet/header.css">
    <link rel="stylesheet" type="text/css" href="../stylesheet/reserve.css">
    <link rel="stylesheet" type="text/css" href="../stylesheet/graph.css">
</head>

<body>

<%
    String uid = request.getParameter("uid");
    String name = request.getParameter("name");

    String eachColor[] = new String[28];
    String scheduleArr[] = new String[28];
    String colorArr[] = {
            "#7BE0AD",
            "#E7E5E5",
            "#E5D0E3",
            "#84D2F6",
            "#E0B0D5",
            "#DDFFF7",
            "#FFA69E",
            "#AA4465",
            "#84D2F6",
            "#462255",

            "#EAC5D8",
            "#DBD8F0",
            "#E2FADB",
            "#84D2F6",
            "#DBEFBC",
            "#963484",
            "#3066BE",
            "#28C2FF",
            "#84D2F6",
            "#2AF5FF",

            "#FCFCFC",
            "#F7567C",
            "#FFFAE3",
            "#84D2F6",
            "#5D576B",
            "#BEB8EB",
            "#5299D3",
            "#0B5563",
    };

    for (int iSchedule = 0; iSchedule < 28; iSchedule++) {
        scheduleArr[iSchedule] = "";
    }

    scheduleArr[1] = "dujin";
    scheduleArr[5] = "pop";
    scheduleArr[8] = "ping";
    scheduleArr[9] = "ping";
    scheduleArr[10] = "ping";

    int cnt = 0;
    String past = "";
    for (int iSchedule = 0; iSchedule < 28; iSchedule++) {
        if (!scheduleArr[iSchedule].equals("")) {
            // arr중에 겹쳤다면 cnt는 안더해줘도 되고 컬러만 바꿔줌
            if (past.equals(scheduleArr[iSchedule])) {

            } else {
                cnt++;
            }
            // list iSchedule 번째를 color 로 색칠
            eachColor[iSchedule] = colorArr[cnt];

            past = scheduleArr[iSchedule];
        } else {
            eachColor[iSchedule] = "#FFFFFF";
        }
    }


%>

<div id="header">
    <div id="top_color_bar"></div>

    <div id="header_tool_bar">
        <div class="container">
            <div id="logo">
                <img id="logo_img" src="../public/images/logo_header.png" />
            </div>
            <form id="logo_form" method="post" action="index.jsp">
                <input type="hidden" name="hiddenvalue" value='go_reserve'>
                <p id="logo_txt" onclick="document.getElementById('logo_form').submit()"><%=Header.getLogoTitle()%></p>
            </form>

            <div>

            </div>

            <form id="mypage_form" method="post" action="index.jsp">
                <input type="hidden" name="hiddenvalue" value='go_mypage'>
                <p id="mypage_txt" onclick="document.getElementById('mypage_form').submit()"><%=Header.getMyPage()%></p>
            </form>

        </div>
    </div>
</div>

<div id="schedule">
    <div id="background"></div>
    <div id="schedule_content" class="content">
        <div id="day">
            <a> 05.27(토) </a>
        </div>
        <div id="show_reserve">
            <h2>오늘의 예약 시간</h2>
            <div id="show_reserve_default_time">
                <h3 id="left_default_time">08:00</h3>
                <h3 id="right_default_time">22:00</h3>
            </div>
            <div id="graph_reserve"></div>
        </div>
        <div id="reserve">
            <div id="circular_graph">
                <div id="graph_box" class="box">
                    <div id="top_graph">
                        <h3>15:00</h3>
                    </div>
                    <div id="horizontal_graph">
                        <div id="left_side_graph">
                            <h3>08:00</h3>
                        </div>
                        <div id="content_graph">
                            <ul class="chart-skills">
                                <%


                                %>
                                <li title="08:00 ~ 08:30" style="border-color:<%=eachColor[0]%>"><span></span></li>
                                <li title="08:30 ~ 09:00" style="border-color:<%=eachColor[1]%>"><span></span></li>
                                <li title="09:00 ~ 09:30" style="border-color:<%=eachColor[2]%>"><span></span></li>
                                <li title="09:30 ~ 10:00" style="border-color:<%=eachColor[3]%>"><span></span></li>
                                <li title="10:00 ~ 10:30" style="border-color:<%=eachColor[4]%>"><span></span></li>
                                <li title="10:30 ~ 11:00" style="border-color:<%=eachColor[5]%>"><span></span></li>
                                <li title="11:00 ~ 11:30" style="border-color:<%=eachColor[6]%>"><span></span></li>
                                <li title="11:30 ~ 12:00" style="border-color:<%=eachColor[7]%>"><span></span></li>
                                <li title="12:00 ~ 12:30" style="border-color:<%=eachColor[8]%>"><span></span></li>
                                <li title="12:30 ~ 13:00" style="border-color:<%=eachColor[9]%>"><span></span></li>
                                <li title="13:00 ~ 13:30" style="border-color:<%=eachColor[10]%>"><span></span></li>
                                <li title="13:30 ~ 14:00" style="border-color:<%=eachColor[11]%>"><span></span></li>
                                <li title="14:00 ~ 14:30" style="border-color:<%=eachColor[12]%>"><span></span></li>
                                <li title="14:30 ~ 15:00" style="border-color:<%=eachColor[13]%>"><span></span></li>
                                <li title="15:00 ~ 15:30" style="border-color:<%=eachColor[14]%>"><span></span></li>
                                <li title="15:30 ~ 16:00" style="border-color:<%=eachColor[15]%>"><span></span></li>
                                <li title="16:00 ~ 16:30" style="border-color:<%=eachColor[16]%>"><span></span></li>
                                <li title="16:30 ~ 17:00" style="border-color:<%=eachColor[17]%>"><span></span></li>
                                <li title="17:00 ~ 17:30" style="border-color:<%=eachColor[18]%>"><span></span></li>
                                <li title="17:30 ~ 18:00" style="border-color:<%=eachColor[19]%>"><span></span></li>
                                <li title="18:00 ~ 18:30" style="border-color:<%=eachColor[20]%>"><span></span></li>
                                <li title="18:30 ~ 19:00" style="border-color:<%=eachColor[21]%>"><span></span></li>
                                <li title="19:00 ~ 19:30" style="border-color:<%=eachColor[22]%>"><span></span></li>
                                <li title="19:30 ~ 20:00" style="border-color:<%=eachColor[23]%>"><span></span></li>
                                <li title="20:00 ~ 20:30" style="border-color:<%=eachColor[24]%>"><span></span></li>
                                <li title="20:30 ~ 21:00" style="border-color:<%=eachColor[25]%>"><span></span></li>
                                <li title="21:00 ~ 21:30" style="border-color:<%=eachColor[26]%>"><span></span></li>
                                <li title="21:30 ~ 22:00" style="border-color:<%=eachColor[27]%>"><span></span></li>

                            </ul>
                        </div>
                        <div id="right_side_graph">
                            <h3>22:00</h3>
                        </div>
                    </div>
                </div>
            </div>
            <form id="reserve_input" method="post">
                <input type="hidden" name="hiddenvalue" value='reserve'>
                <div id="wrapper_reserve_form" class="box">
                    <p>시작시간</p>
                    <select class="selector_border" name="start">
                        <option>08:00</option>
                        <option>08:30</option>
                        <option>09:00</option>
                        <option>09:30</option>
                        <option>10:00</option>
                        <option>10:30</option>
                        <option>11:00</option>
                        <option>11:30</option>
                        <option>12:00</option>
                        <option>12:30</option>
                        <option>13:00</option>
                        <option>13:30</option>
                        <option>14:00</option>
                        <option>14:30</option>
                        <option>15:00</option>
                        <option>15:30</option>
                        <option>16:00</option>
                        <option>16:30</option>
                        <option>17:00</option>
                        <option>17:30</option>
                        <option>18:00</option>
                        <option>18:30</option>
                        <option>19:00</option>
                        <option>19:30</option>
                        <option>20:00</option>
                        <option>20:30</option>
                        <option>21:00</option>
                        <option>21:30</option>
                    </select>
                    <br>
                    <p>사용시간</p>
                    <select class="selector_border" name="time">
                        <option>30 min</option>
                        <option>60 min</option>
                        <option>90 min</option>
                        <option>120 min</option>
                    </select>
                    <br>
                    <br>
                    <input class="btn btn-blue" type="submit" value="Reserve">
                </div>
            </form>
        </div>
    </div>
</div>

</body>
</html>
