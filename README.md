# TcpServers
 Here are two TCP projects, one implemented in C and the other in Python. In the C project, the server encrypts messages received from the client using a Caesar cipher before saving them. The Python project involves a chat room server where users can log in and exchange messages with one another.

To run the C program, you need to compile and execute the server and client code in two separate terminals.
For server: 
gcc -o server server.c
./server
For client:
gcc -o client client.c
./client


To run the Python code, begin by starting the server with the following command:
python3.12 server.py
Next, connect multiple clients, each in their own terminal, using the command:
python3.12 client.py
