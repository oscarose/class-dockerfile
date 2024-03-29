FROM centos:7

RUN     yum -y update && \
    yum -y install wget && \
    yum -y install tar.x86_64 && \
    yum clean all

USER root

ARG HTTP_PORT=8080
ARG INSTALL_DIR=/opt
ARG JAVA_NAME=jdk1.8.0_331
ENV JAVA_HOME /opt/jdk1.8.0_331
ENV CATALINA_PID /opt/apache-tomcat-8.5.76/temp/tomcat.pid
ENV CATALINA_HOME /opt/apache-tomcat-8.5.76

COPY jdk-8u331-linux-x64.tar.gz ${INSTALL_DIR}
COPY apache-tomcat-8.5.76.tar.gz ${INSTALL_DIR}
RUN cd ${INSTALL_DIR} && tar -xzvf jdk-8u331-linux-x64.tar.gz
RUN alternatives --install /usr/bin/java java ${INSTALL_DIR}/${JAVA_NAME}/bin/java 2
RUN alternatives --install /usr/bin/jar jar ${INSTALL_DIR}/${JAVA_NAME}/bin/jar 2
RUN alternatives --install /usr/bin/javac javac ${INSTALL_DIR}/${JAVA_NAME}/bin/javac 2
RUN alternatives --set jar ${INSTALL_DIR}/${JAVA_NAME}/bin/jar
RUN alternatives --set javac ${INSTALL_DIR}/${JAVA_NAME}/bin/javac
RUN export JAVA_HOME=${INSTALL_DIR}/${JAVA_NAME}
RUN export JRE_HOME=${INSTALL_DIR}/${JAVA_NAME}/jre
RUN export PATH=$PATH:${INSTALL_DIR}/${JAVA_NAME}/bin:${INSTALL_DIR}/${JAVA_NAME}/jre/bin
RUN echo "PATH=$PATH:/opt" >> /root/.bash_profile
RUN cd ${INSTALL_DIR} && tar -xzvf apache-tomcat-8.5.76.tar.gz
RUN mkdir ${INSTALL_DIR}/apache-tomcat-8.5.76/conf/Catalina && mkdir ${INSTALL_DIR}/apache-tomcat-8.5.76/conf/Catalina/localhost
COPY jenkins.war ${INSTALL_DIR}/apache-tomcat-8.5.76/webapps
COPY tomcat-users.xml ${INSTALL_DIR}/apache-tomcat-8.5.76/conf
COPY manager.xml ${INSTALL_DIR}/apache-tomcat-8.5.76/conf/Catalina/localhost

EXPOSE ${HTTP_PORT}

CMD /opt/apache-tomcat-8.5.76/bin/startup.sh run && tail -f /opt/apache-tomcat-8.5.76/logs/catalina.out
