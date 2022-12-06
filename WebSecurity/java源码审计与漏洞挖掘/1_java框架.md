# Java 框架

## 概述

1. Spring 
   - IOC, Inversion of Control, 控制反转, (DI: Dependency Injection)
   - AOP, Aspect Orient Programming

2. Spring MVC
   - 用户发起请求 -> Spring MVC DispatcherServlet -> HandlerMappig -> Controller
   - Controller 处理业务逻辑, 返回执行结果
   - ViewResolver 解析 Controller 返回结果 -> 前端DispatcherServlet解析 -> View 对象
   - DispatcherServlet 对 view进行渲染, 返回给浏览器, 完成请求交互

3. Spring Boot, 更集成
4. Struts2
5. SSH: Struts2 Spring Hibernate
6. SSM: SpringMVC Spring MyBatis

7. reference
   - [IoC原理](https://www.liaoxuefeng.com/wiki/1252599548343744/1282381977747489)
   - [AOP](https://welson327.gitbooks.io/java-spring/content/spring_aop/aop.htm)

## Spring

1. 架构
   - Tomcat 容器
   - Filter
   - Servlet
   - Interceptor
   - Controller

### SSH vs SSM

1. Struts2 vs SprintMVC
   - SpringMVC与Spring的兼容性更好些
2. Hibernate vs Mybatis
   - Mybatis 入门更容易, 更灵活
   - Hibernate 封装性更好, SQL 优化有欠缺, 学习成本也高一些, 优化难度较高

### 常见web容器
    - Apache
    - Tomcat
    - JBOSS
    - Jetty
    - Nginx

