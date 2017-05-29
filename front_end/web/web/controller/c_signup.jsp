<%--
  Created by IntelliJ IDEA.
  User: clucle
  Date: 2017-05-29
  Time: 오전 12:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    request.setCharacterEncoding("UTF-8");
    String uid = request.getParameter("uid");
    String pw = request.getParameter("pw");
    String name = request.getParameter("name");

    request.setAttribute("uid", uid);
    request.setAttribute("pw", pw);
    request.setAttribute("name", name);

    pageContext.forward("../view/reserve.jsp");

    //response.sendRedirect("../view/reserve.jsp");
%>