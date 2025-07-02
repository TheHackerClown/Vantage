#!/usr/bin/env python

from tkinter import ttk, Tk,PhotoImage,Menu
from pathlib import Path
from tkinter.messagebox import showwarning as warn


ESI_EMPLOYEE_RATE = 0.75
EPF_EMPLOYEE_RATE = 12.0
ESI_EMPLOYER_RATE = 3.25
EPF_EMPLOYER_RATE = 13.0



class Vantage(Tk):
    #Initialization
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args,**kwargs)
        self.file_dir = Path(__file__).resolve().parent


        #Title
        self.wm_title("Vantage Payroll")
        
        #Logo
        self.logo_png = PhotoImage((self.file_dir / "assets/Vantage.png").as_posix())
        self.iconphoto(True,self.logo_png)
        
        #Taskbar Logo (Windows Specific)
        try:
            self.logo_ico = PhotoImage((self.file_dir / "assets/Vantage.ico").as_posix())
            self.iconbitmap(self.logo_ico)
        except Exception as e:
            pass

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        #Theme
        self.tk.call('source', self.file_dir / 'assets/theme/forest-light.tcl')
        ttk.Style().theme_use('forest-light')
        self.protocol("WM_DELETE_WINDOW",lambda:warn("Close Button Clicked","Use Exit Button to safely close this Software."))
        self.resizable(False,False)

        #Initialize the top menu bar and draw the main window content
        self.topMenuBar()
        self.drawWindow()


    #Initialization of the top menu bar
    def topMenuBar(self):
        self.menubar = Menu(self)

        selectionMenu = Menu(self.menubar, tearoff=0)
        selectionMenu.add_command(label="Exit",command=self.quit)
        selectionMenu.add_separator()
        self.menubar.add_cascade(label="Selection", menu=selectionMenu)

        masterMenu = Menu(self.menubar, tearoff=0)
        masterMenu.add_command(label="Exit",command=self.quit)
        masterMenu.add_separator()
        self.menubar.add_cascade(label="Master", menu=masterMenu)

        datamaintainMenu = Menu(self.menubar, tearoff=0)
        datamaintainMenu.add_command(label="Exit",command=self.quit)
        datamaintainMenu.add_separator()
        self.menubar.add_cascade(label="Data Maintenance", menu=datamaintainMenu)
        
        reportsMenu = Menu(self.menubar, tearoff=0)
        reportsMenu.add_command(label="Exit",command=self.quit)
        reportsMenu.add_separator()
        self.menubar.add_cascade(label="Reports", menu=reportsMenu)

        updationMenu = Menu(self.menubar, tearoff=0)
        updationMenu.add_command(label="Exit",command=self.quit)
        updationMenu.add_separator()
        self.menubar.add_cascade(label="Updation", menu=updationMenu)

        setupMenu = Menu(self.menubar, tearoff=0)
        setupMenu.add_command(label="Exit",command=self.quit)
        setupMenu.add_separator()
        self.menubar.add_cascade(label="Setup", menu=setupMenu)

        quitMenu = Menu(self.menubar, tearoff=0)
        quitMenu.add_command(label="Exit",command=self.quit)
        quitMenu.add_separator()
        self.menubar.add_cascade(label="Quit",menu=quitMenu)

        self.disableMenu(menu_handle="Selection")
        self.config(menu=self.menubar)

    # Disable a menu item
    def disableMenu(self, menu_handle=None, menu_name=None):
        if not menu_handle:
            if not menu_name:
                return
            self.menubar.entryconfig(menu_name, state="disabled")
        else:
            if not menu_name:
                return
            menu_handle.entryconfig(menu_name, state="disabled")

    # Enable a menu item
    def enableMenu(self, menu_handle=None, menu_name=None):
        if not menu_handle:
            if not menu_name:
                return
            self.menubar.entryconfig(menu_name, state="normal")
        else:
            if not menu_name:
                return
            menu_handle.entryconfig(menu_name, state="normal")


    # Draw the main window content
    # Tab System to be implemented later
    def drawWindow(self):
        button = ttk.Button(self, text="Welcome to Vantage")
        button.pack(pady=20)


if __name__ == "__main__":
    vantageApp = Vantage()
    vantageApp.mainloop()