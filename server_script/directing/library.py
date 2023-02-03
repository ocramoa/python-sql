import datetime

class Librarian():
    """This class deals with the server history file. It also contains the url of the repo and the available operations.
    
    Librarian can update, get, and delete the server history.
    
    Attributes:
        _history -> Data about the current client's connection to be stored in history.txt.
        _users -> Essentially just a list of valid usernames the client can use.
        _url -> Instructions on how to get the server code.
        _data_path -> File path of the history.txt file.
        _operations -> Instructions on how to interact with the server. Will be moved to another object in the near future.
    """

    def __init__(self):
        self._history = {}
        self._users = ["kaedon","bagelforever","admin"]
        self._url = "https://github.com/ocramoa/pysqlsimpleserver.git"
        self._data_path = r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt"
        self._operations = "1 for CREATE. 2 for READ. 3 for UPDATE. 4 for DELETE. 5 for INSERT."

    def update_history(self, client, time):
        """Updates the server history."""
        self._history.update({client:time})
        # After updating the _history attribute, opens the file and appends it.
        with open(self._data_path, "a") as h:
            h.write(f"{self._history}\n")

    def get_history(self):
        """Gets the server access history."""
        with open(self._data_path, "r") as h:
            # Simply reads and returns the contents of the entire file. In a larger project, this would be unwise.
            record = h.read()
        
        return record

    def delete_history(self, n):
        """Deletes the server's history at n. Copied from https://pynative.com/python-delete-lines-from-file, with minor changes."""
        with open(self._data_path, "r+", encoding="utf-8") as h:
            
            # read an store all lines into list
            lines = h.readlines()
            # move file pointer to the beginning of a file
            h.seek(0)
            # truncate the file
            h.truncate()

            # start writing lines
            # iterate line and line number
            for number, line in enumerate(lines):
                # delete line number
                if number != (n - 1):
                    h.write(line)

    def delete_all(self, client):
        """Deletes all server access history and replaces it with a deleted notice."""
        with open(self._data_path, "w+") as h:
            # Because we open the file in write+ mode, it deletes everything there and writes who deleted it and when.
            h.write(f"delete_all by {client} at {datetime.datetime.now()}\n")