import mysql.connector
from server_script.operations.maintainer import Maintainer

class Read(Maintainer):
    """Takes the user's input and reads from the database. Inherits from Maintainer.

    Attributes:
        _is_err (bool): Whether or not an error ocurred during execution of the query.
    """
    def __init__(self):
        super().__init__()
        self._is_err = False

    def read(self, password, database, input):
        # Establish a connection using the client-provided data and password. Note that this does use the root user.
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=f"{password}",
            database=f"{database}"
        )
        
        # cursor object c
        c = db.cursor()
        
        # example select statement for tblemployee which returns all columns
        # employeetbl_select = """SELECT * FROM tblemployee"""

        tbl_select = f"""{input}"""
        
        try:
            # execute the select query to fetch all rows  
            c.execute(tbl_select)
        
            # fetch all the data returned by the database
            data = c.fetchall()
        except mysql.connector.Error as err:
            db.close()
            self._is_err = True
            err_msg = "Could not read from database. {}".format(err)
            return err_msg
        
        # if you want, you can print all the data returned by the database this way:
        # for e in data:
        #     print(e)
        
        # finally closing the database connection
        db.close()

        with open(r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt", "a") as h:
            h.write(f"{tbl_select}\n")

        return data