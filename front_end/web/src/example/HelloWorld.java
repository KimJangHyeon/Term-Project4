package example;

import java.io.*;
import javax.servlet.*;
/**
 * Created by clucle on 2017-05-23.
 */
public class HelloWorld {
  public String sayHelloWorldFrom(String from) {
    String result = "Hello, world, from " + from;
    System.out.println(result);
    return result;
  }
  public static String show() {
    return "Hello World";
  }


}
