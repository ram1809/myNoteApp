FROM tomcat:9.0
WORKDIR /root/myNoteApp
ENTRYPOINT apachectl -D FOREGROUND
COPY /root/myNoteApp /usr/local/tomcat/webapps
