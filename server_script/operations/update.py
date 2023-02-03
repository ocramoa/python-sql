import mysql.connector
from server_script.operations.maintainer import Maintainer

class Update(Maintainer):
    """Takes the user's input and updates a table or tables with it. Inherits from Maintainer.

    Attributes:
        _is_err (bool): Whether or not an error ocurred during execution of the query.
        msg (string): The message returned by the create method.
    """
    def __init__(self):
        super().__init__()
        self._is_err = False
        self.msg = ""

    def update(self, password, database, input):
        # Establish a connection using the client-provided data and password. Note that this does use the root user.
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=f"{password}",
            database=f"{database}"
        )
        
        # cursor object c
        c = db.cursor()
        
        # example update statement for tblemployee
        # which modifies the salary of first employee
        # employeetbl_update = "UPDATE tblemployee\
        # SET salary = 115000 WHERE empid = 1"

        tbl_update = f"""{input}"""
        
        try:    
            c.execute(tbl_update)
            db.commit()
        except mysql.connector.Error as err:
            db.close()
            self._is_err = True
            self.msg = "Could not update. {}".format(err)
            return self.msg

        # finally closing the database connection
        db.close()

        with open(r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt", "a") as h:
            h.write(f"{tbl_update}")

        self.msg = "Update command successful."
        return self.msg