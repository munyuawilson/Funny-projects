The program simulates a real web server and a client.

Direct Mode

First run the server.py before running client.py

Server.py file

This python file consists of code that make up the local machine server. The server receives requests from the client.py program.

The imbedded socket library in Python will assist in this implementation.

Constants

This constants are used in both files.

Declaration of constant values such as:

port=8000

Can declare port value of your preference.

host=socket.gethostname()

This is the host machine.

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
