import mysql.connector
from server_script.operations.maintainer import Maintainer

class Insert(Maintainer):
    """Responsible for taking the user's input and inserting data into a table (or tables) with it. Inherits from Maintainer.

    Attributes:
        _is_err (bool): Whether or not an error ocurred during execution of the query.
        msg (string): The message returned by the create method.
    """
    def __init__(self):
        super().__init__()
        self._is_err = False
        self.msg = ""

    def insert(self, password, database, input):
        # Establish a connection using the client-provided data and password. Note that this does use the root user.
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=f"{password}",
            database=f"{database}"
        )
        
        # cursor object c
        c = db.cursor()
        
        # example insert statement for tblemployee
        # this statement will enable us to insert multiple rows at once.
        # employeetbl_insert = """INSERT INTO tblemployee (
        # empname,
        # department,
        # salary)
        # VALUES  (%s, %s, %s)"""
        
        # example data
        # we save all the row data to be inserted in a data variable
        # data = [("Vani", "HR", "100000"),
        #         ("Krish", "Accounts", "60000"),
        #         ("Aishwarya", "Sales", "25000"),
        #         ("Govind", "Marketing", "40000")]

        tbl_insert = f"""{input}"""
        
        # execute the insert commands for all rows and commit to the database
        try:
            c.execute(tbl_insert)
            db.commit()
        except mysql.connector.Error as err:
            db.close()
            self._is_err = True
            self.msg = "Failed to insert. {}".format(err)
            return self.msg
        
        # finally closing the database connection
        db.close()

        with open(r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt", "a") as h:
            # h.write(f"{tbl_insert}, {data_to_list}\n")
            h.write(f"{tbl_insert}\n")

        self.msg = "Insert command successful."
        return self.msg