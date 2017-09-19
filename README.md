# SimplePyHttpServer
Simple http server in python that honor GET, POST method with custom implementation.

You can run this on Linux and Windows as well. You must have python 2.7 installed on your system in order to run the server.

PyHttpServer.py - This file is entry point to run the server. Default port is 80, you should change port if needed in this file. <br>
HttpServerImpl.py - This file contains the implementation of GET and POST method, those are left to the user to implement as per need.<br>

This implementation support only JSON format for POST method data. But you can free to change the implementation as per your need to honor wide range of data formats.

Run server using below command

    python PyHttpServer.py
    
Or you can run script in deamon mode on Linux.

This server can be useful many ways depends on your requirement or usage and how you implement the GET, POST function in order to get your work done.
- instant demo purpose, desired request and response.
- you can implement methods to perform some frequently used command (like memory state of server, is particular process alive, searched text in logs for debugging perpose.. etc.) on one particular server from your browser.

Testing default implementation:

POST:

      curl -d '{"eid":"1231"}' localhost
GET:

     curl -i http://localhost/?command=ifconfig
     
     OR
     
     Hit http://localhost/?command=ifconfig url in web browser.
     
Feel free to write me an email.
