<%@ page import="component.Header" %><%--
  Created by IntelliJ IDEA.
  User: clucle
  Date: 2017-05-28
  Time: 오후 11:52
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="../stylesheet/header.css">
    <link rel="stylesheet" type="text/css" href="../stylesheet/sign_in_up.css">
</head>

<body>

<div id="header">
    <div id="top_color_bar"></div>

    <div id="header_tool_bar">
        <div class="container">
            <div id="logo">
                <img id="logo_img" src="../public/images/logo_header.png" />
            </div>
            <p id="logo_txt">예약 시스템</p>

            <form id="signup_form" method="post" action="index.jsp">
                <input type="hidden" name="hiddenvalue" value='go_signup'>
                <p id="signup_txt" onclick="document.getElementById('signup_form').submit()"><%=Header.getSignUp()%></p>
            </form>

        </div>
    </div>
</div>

<div id="sign_up">
    <div id="background" />

    <div id="signup_content" class="content">
        <div id="wrapper_login_form" class="box">

            <form id="login_form" method="post">
                <a>예약 시스템에 로그인합니다</a>
                <input type="hidden" name="hiddenvalue" value='signin'>
                <br>
                <label for="uid">ID</label>
                <input class="input_border" type="text" name="uid" id="uid"><br>
                <label for="pw">Password</label>
                <input class="input_border" type="password" name="pw"id="pw"><br><br>
                <input class="btn btn-blue" type="submit" value="Sign In">
            </form>
        </div>
    </div>
</div>

</body>
</html>