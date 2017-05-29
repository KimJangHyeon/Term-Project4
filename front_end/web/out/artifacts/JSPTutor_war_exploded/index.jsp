<%@ page import="example.HelloWorld" %><%--
  Created by IntelliJ IDEA.
  User: clucle
  Date: 2017-05-23
  Time: 오후 12:48
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%
    request.setCharacterEncoding("UTF-8");
    try {
        String type = request.getParameter("hiddenvalue");

        if (type.equals("signup")) {
            String uid = request.getParameter("uid");
            String pw = request.getParameter("pw");
            String name = request.getParameter("name");

            request.setAttribute("uid", uid);
            request.setAttribute("pw", pw);
            request.setAttribute("name", name);

            pageContext.forward("view/reserve.jsp");
        } else if (type.equals("signin")) {
            String uid = request.getParameter("uid");
            String pw = request.getParameter("pw");

            request.setAttribute("uid", uid);
            request.setAttribute("pw", pw);

            pageContext.forward("view/reserve.jsp");
        }
        else if (type.equals("go_signin")) {
            pageContext.forward("view/signin.jsp");
        }
        else if (type.equals("go_signup")) {
            pageContext.forward("view/signup.jsp");
        }

    } catch (Exception e) {
        pageContext.forward("view/signup.jsp");
    }

%>