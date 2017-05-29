<%@ page import="component.Header" %><%--
  Created by IntelliJ IDEA.
  User: clucle
  Date: 2017-05-29
  Time: 오후 10:21
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
        }
    </style>

    <link rel="stylesheet" type="text/css" href="../stylesheet/header.css">
    <link rel="stylesheet" type="text/css" href="../stylesheet/mypage.css">
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


<div id="mypage">

    <div id="background"></div>
    <div id="mypage_content" class="content">

        <a>예약한 시간</a>

        <table class="type07">
            <thead>
            <tr>
                <th scope="cols">날짜</th>
                <th scope="cols">방 번호</th>
                <th scope="cols">시작 시각</th>
                <th scope="cols">종료 시각</th>
                <th scope="cols">삭제</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">2017-05-28</th>
                <td>0</td>
                <td>08:00</td>
                <td>09:00</td>
                <td>v</td>

            </tr>
            <tr>
                <th scope="row">2017-05-28</th>
                <td>0</td>
                <td>08:00</td>
                <td>09:00</td>
                <td>v</td>

            </tr>

            </tbody>
        </table>

    </div>

</div>
</body>
</html>
