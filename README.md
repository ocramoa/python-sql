# Overview

Before you proceed, know that this project is unfinished. There's a lot left to do and test.

This is an extension of the simpleserver project that performs CRUD operations on a MySQL database.

When run (via main), the server will run forever until it is manually stopped via Ctrl+C. It listens continuously for a request from the client in the form of an operation number followed by other arguments.  Upon receiving a request, the server immediately logs the client's request in the history.txt file and prints it to the server terminal. The server always sends back whether or not the operation was successful and why, and can also send a response based on what the user decides to do with the history.txt file.

This is an experimental project designed to teach myself how to interface with MySQL with Python 3.11.

# Requirements

To run the server, you'll need Python 3 and the mysql.connector module. You'll also need the MySQL service, with databases you can either download or create on your own. While testing this project, I used an example database called employee_db I created with some help from the Internet, along with the sakila database. There is no functionality yet in the client or server for creating a database.

To run the client, all you'll need is Python 3 with the tkinter and socket modules installed.

I have only tested this project over LAN, so you might run into problems if you connect from a different network.

# Network Communication

I used client-server architecture. The server receives requests from clients, services them, and sends back data. However, this simple server can only service one request at a time. Multithreading will be added soon.

This is a TCP server as UDP is not necessary for something this small and slow. I used port 5007, but any other random unused port will do.

Both the client and server communicate with byte-like messages. They convert a string message to byte-like before sending data and do the reverse after receiving data. The client should always use this format -- "number|password|database" followed by your query in the text window that appears. You will easily break the program if you type something different.

# Development Environment

I developed this program with Visual Studio Code and the command line on a Windows PC and a Chromebook running Linux.

For the code itself, I used Python 3.11 and the socket, socketserver and datetime libraries. I also used mysql.connector and the tkinter library.

# Useful Websites

* [Python 3 socket](https://docs.python.org/3.11/library/socket.html)
* [Python 3 socketserver](https://docs.python.org/3/library/socketserver.html)
* [StackOverflow: Difference between modes a, a+, w, w+, and r+ in built-in open function? by flybywire](https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function)
* [Delete Lines from a File in Python](https://pynative.com/python-delete-lines-from-file/)

# Future Work

* The server should use multithreading to service up to 10 clients at once. Of course, this gets complicated fast. I need to learn more about locks in MySQL to do this.
* Again, I actually could not figure out how to get the server to sendall multiple times when variables in f-strings were involved. Although I like the way it looks now, if I wanted to spend more time on this I'd dig deeper and find out why.
* Again, it would be nice if the client could do more with the server. Perhaps the server could generate and store a unique username for the client to use in operations.

# Known Issues

* Inserting too many values at once into a table can break the program.
* I haven't tested a lot. It could break during normal ops.