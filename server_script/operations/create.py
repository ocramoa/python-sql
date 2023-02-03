import mysql.connector
from server_script.operations.maintainer import Maintainer

class Create(Maintainer):
    """Responsible for taking the user's input and creating a table with it. Inherits from Maintainer.
    
    Attributes:
        _is_err (bool): Whether or not an error ocurred during execution of the query.
        msg (string): The message returned by the create method.
    """

    def __init__(self):
        """Constructs a new Creator."""
        super().__init__()
        self._is_err = False
        self.msg = ""

    def create(self, password, database, input):
        # Establish a connection using the client-provided data and password. Note that this does use the root user.
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=f"{password}",
        database=f"{database}"
        )
    
        # cursor object c
        c = db.cursor()
    
        # example create statement for tblemployee
        # employeetbl_create = """CREATE TABLE `employee_db`.`tblemployee` (
        # `empid` INT NOT NULL AUTO_INCREMENT,
        # `empname` VARCHAR(45) NULL,
        # `department` VARCHAR(45) NULL,
        # `salary` INT NULL,
        # PRIMARY KEY (`empid`))"""

        tbl_create = f"""{input}"""
        
        try:
            c.execute(tbl_create)
        except mysql.connector.Error as err:
            db.close()
            self._is_err = True
            self.msg = "Failed to create table. {}".format(err)
            return self.msg
        
        # closing the database connection
        db.close()

        with open(r"C:\Users\eyeba\python_code\python-sql\server_script\data\history.txt", "a") as h: 
            h.write(f"{tbl_create}\n")

        self.msg = "Create command successful."
        return self.msg