import socket
from services.gui import RootWindow

#TODO: A lot of work. Create a GUI for the client and format the messages received better.

HOST, PORT = "192.168.0.245", 5007

initial_input = input("CRUD+INSERT. 1-5 corresponding to operation. \n Enter arguments in this format 'int(1<->5)|psswrd|db'. Afterwards you will be prompted for your SQL query.\n Write here: ")
print(initial_input)
entry_window = RootWindow()

while True:
    entry_window.mainloop()
    if entry_window.input_text != "":
        operation = entry_window.input_text
        break

print(operation)

data = f"{initial_input}|{operation}"

print(data)

# Much of this is from the documentation for socketserver. I have changed only a little bit.
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down. Increased byte size to just over 2KB because the history can get large. Hard limit on reading data.
    received = str(sock.recv(2048), "utf-8")

# Print the data sent and received to the terminal.
print("Sent:     {}".format(data))
print("Received: {}".format(received))