<%@ page import="component.Header" %>
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
                        <h3>13:00</h3>
                    </div>
                    <div id="horizontal_graph">
                        <div id="left_side_graph">
                            <h3>08:00</h3>
                        </div>
                        <div id="content_graph">
                            <ul class="chart-skills">
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>
                                <li><span></span></li>

                            </ul>
                        </div>
                        <div id="right_side_graph">
                            <h3>22:00</h3>
                        </div>
                    </div>
                </div>
            </div>
            <div id="reserve_input">
                <div id="wrapper_reserve_form" class="box">
                    <p>시작시간</p>
                    <select class="selector_border" name="start">
                        <option>08:00</option>
                        <option>08:30</option>
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
            </div>
        </div>
    </div>
</div>

</body>
</html>
