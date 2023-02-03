from tkinter import *

class RootWindow(Tk):
    """Creates the root window for the SQL submission. Needs to be cleaned up, but works."""

    def __init__(self):
        super().__init__()
        
        # I realize this is the messiest thing known to man. I will fix it. Maybe
        self.geometry("300x300")
        self.title("SQL Text Entry")
        self.minsize(height=560, width=560)
        self.maxsize(height=250, width=350)
        self.input_text = ""
        # scroll bar
        self.scrollbar = Scrollbar(self)
        # pack scrollbar
        self.scrollbar.pack(side=RIGHT,fill=Y)
        # make text box
        self.text_info = Text(self, yscrollcommand=self.scrollbar.set)
        self.text_info.pack(fill=BOTH)
        # config scrollbar
        self.scrollbar.config(command=self.text_info.yview)
        # create button for submittal
        self.printButton = Button(self,
                        text = "Submit (Don't use semicolon to end)", 
                        command = self.getInput)

        self.printButton.pack()

    def getInput(self):
        inp = self.text_info.get(1.0, "end-1c")
        self.input_text = inp
        self.destroy()

        return self.input_text