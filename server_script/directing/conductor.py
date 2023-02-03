import socketserver
import datetime
from server_script.directing.library import Librarian
from server_script.operations.create import Create
from server_script.operations.read import Read
from server_script.operations.update import Update
from server_script.operations.delete import Delete
from server_script.operations.insert import Insert

class Conductor(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.

    The above is in the default documentation for the base request handler.
    """

    def handle(self):
        # Instantiate the Librarian class.
        librarian = Librarian()
        # self.request is the TCP socket connected to the client. 
        self.data = self.request.recv(2048).strip()
        # Decode bytelike data to utf-8.
        decoded = self.data.decode("utf-8")
        # Split on pipe character to store the user and their operations into a list. This is safe because the client does not use command-line arguments.
        user_args = decoded.split("|")
        print(f"{self.client_address[0]} wrote:")
        print(user_args)
        print(f"at {datetime.datetime.now()}")
        #After printing to terminal, update the history.txt file with request data. Then print data about the current connection.
        librarian.update_history(self.client_address[0],str(datetime.datetime.now()))
        print(librarian._history)
        # If the operation is valid, accept their argument if it exists and perform the associated action.
        # example request: 1|pswrd|employee_db|input

        if user_args[0] in ["1","2","3","4","5","h"]:
            print()
            # This response variable is what will be sent to the client later.
            response = ""
            if len(user_args) < 4:
                self.request.sendall(bytes("Number of arguments too low. Example request: 1|pswrd|employee_db|input.", "utf-8"))
            else:
                # If the user wants to create the table, instantiate the Create class and pass its only function the user's arguments.
                if user_args[0] == "1":
                    creator = Create()
                    creator.create(user_args[1],user_args[2],user_args[3])
                    if creator._is_err == False:    
                        response = "Table created."
                    else:
                        response = "Error in your SQL. {}".format(creator.msg) #Send back the error if something broke. I do this for the rest of the operations as well.
                
                # Unlike the others, the Read operation does not store a string in response -- instead it returns the raw result of the select query.
                elif user_args[0] == "2":
                    reader = Read()  
                    response = reader.read(user_args[1],user_args[2],user_args[3]) 
                
                elif user_args[0] == "3":
                    updater = Update()
                    updater.update(user_args[1],user_args[2],user_args[3])
                    if updater._is_err == False:
                        response = "Table updated."
                    else:
                        response = "Error in your SQL. {}".format(updater.msg)
                
                # The delete method is a "hard" deletion of data. Another method could be created in the future to toggle activity status as a "soft" deletion.
                elif user_args[0] == "4":
                    deleter = Delete()
                    deleter.delete(user_args[1],user_args[2],user_args[3])
                    if deleter._is_err == False:
                        response = "Data in table hard deleted."
                    else:
                        response = "Error in your SQL. {}".format(deleter.msg)
                
                # Insert takes an additional parameter -- values. Values should be sent as a raw list of tuples.
                elif user_args[0] == "5":
                    inserter = Insert()
                    inserter.insert(user_args[1],user_args[2],user_args[3],user_args[4])
                    if inserter._is_err == False:
                        response = "Data inserted into table."
                    else:
                        response = "Error in your SQL. {}".format(inserter.msg)
                
                # Hidden method for viewing, updating and deleting server history. Use this format: h|user|operation|line number if deleting, otherwise a random integer to keep from failing length check. I haven't checked if this works yet
                elif user_args[0] == "h" and user_args[1] in librarian.users:
                    
                    # Delete history at line number
                    if user_args[2] == "1":
                        librarian.delete_history(int(user_args[3]))
                        librarian.update_history(f"{user_args[1]}", f"Deleted at: {user_args[3]}")
                        response = f"\nHistory at {user_args[3]} deleted by {user_args[1]}."
                    
                    # Get history
                    elif user_args[2] == "2":
                        hehe_gottem = librarian.get_history()
                        response = f"{hehe_gottem}"
                        librarian.update_history(self.client_address[0],(user_args[0] + " got history at " + str(datetime.datetime.now())))
                    
                    # Delete all history. Should do this regularly
                    elif user_args[2] == "3":
                        librarian.delete_all(user_args[0])
                        response = "All history deleted."
                    
                    else:
                        response = "Either no operation or operation is invalid."
                
                self.request.sendall(bytes(f"\n{response}", "utf-8"))