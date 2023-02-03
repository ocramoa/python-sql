import mysql.connector
from server_script.operations.maintainer import Maintainer

class Delete(Maintainer):
    """Responsible for taking the user's input and deleting data from a table with it. Inherits from Maintainer.

    Attributes:
        _is_err (bool): Whether or not an error ocurred during execution of the query.
        msg (string): The message returned by the create method.
    """
    def __init__(self):
        super().__init__()
        self._is_err = False
        self.msg = ""

    def delete(self, password, database, input):
        # Establish a connection using the client-provided data and password. Note that this does use the root user.
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=f"{password}",
            database=f"{database}"
        )
        
        # cursor object c
        c = db.cursor()
        
        # example delete statement for tblemployee
        # which deletes employee Aishwarya having empid 3
        # employeetbl_delete = "DELETE FROM tblemployee WHERE empid=3"

        tbl_delete = f"""{input}"""
        
        # execute the delete statement and commit to the database
        try:    
            c.execute(tbl_delete)
            db.commit()
        except mysql.connector.Error as err:
            db.close()
            self._is_err = True
            self.msg = "Could not delete. {}".format(err)
            return self.msg
        
        # finally closing the database connection
        db.close()

        with open(r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt", "a") as h:
            h.write(f"{tbl_delete}\n")

        self.msg = "Delete command successful."
        return self.msg