#!/usr/bin/env python

from tkinter import ttk, Tk,PhotoImage,Menu
from pathlib import Path
from tkinter.messagebox import showwarning as warn

#Initializations
file_dir = Path(__file__).resolve().parent

class Vantage(Tk):
    #Initialization
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args,**kwargs)

        #Title
        self.wm_title("Vantage Payroll")
        
        #Logo
        self.logo_png = PhotoImage((file_dir / "assets/Vantage.png").as_posix())
        self.iconphoto(True,self.logo_png)
        
        #Taskbar Logo (Windows Specific)
        try:
            self.logo_ico = PhotoImage((file_dir / "assets/Vantage.ico").as_posix())
            self.iconbitmap(self.logo_ico)
        except Exception as e:
            pass

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        self.tk.call('source', file_dir / 'assets/theme/forest-light.tcl')
        ttk.Style().theme_use('forest-light')
        self.protocol("WM_DELETE_WINDOW",lambda:warn("Close Button Clicked","Use Exit Button to safely close this Software."))
        self.resizable(False,False)


        self.topMenuBar()
        self.drawWindow()

    def topMenuBar(self):
        menubar = Menu(self)

        selectionMenu = Menu(menubar, tearoff=0)
        selectionMenu.add_command(label="Exit",command=self.quit)
        selectionMenu.add_separator()
        menubar.add_cascade(label="Selection", menu=selectionMenu)


        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="Exit",command=self.quit)
        helpMenu.add_separator()
        menubar.add_cascade(label="Help",menu=helpMenu)

        self.config(menu=menubar)

    def drawWindow(self):
        button = ttk.Button(self, text="Welcome to Vantage")
        button.pack(pady=20)


if __name__ == "__main__":
    vantageApp = Vantage()
    vantageApp.mainloop()