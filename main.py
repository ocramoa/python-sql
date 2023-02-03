import socketserver
from server_script.directing.conductor import Conductor

# Start the server here.

if __name__ == "__main__":
    # Replace this host and port with a different one if you'd like. The host should be the IP address of the machine running the server code.
    HOST, PORT = "192.168.0.245", 5007
    conductor = Conductor

    # Create the server, binding to the host and port.
    # Make sure the MySQL service is also running.
    with socketserver.TCPServer((HOST, PORT), conductor) as server:
        # Activate the server; this will keep running until you interrupt the program with Ctrl-C
        server.serve_forever()