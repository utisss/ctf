FROM tomcat:7.0.88-alpine

COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

COPY context.xml /usr/local/tomcat/webapps/manager/META-INF

COPY web.xml /usr/local/tomcat/webapps/manager/WEB-INF/web.xml

CMD ["catalina.sh", "run"]
