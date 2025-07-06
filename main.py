#!/usr/bin/env python

from tkinter import ttk, Tk,PhotoImage,Menu
from pathlib import Path
from tkinter.messagebox import showwarning as warn, showinfo as info


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
        self.companytitle = "G. P. Singh And Associates"
        self.month = "January, 2024"
        self.refreshTitle()


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

        #--------------------------------------------------------

        selectionMenu = Menu(self.menubar, tearoff=0)

        selectionMenu.add_command(label="Select", command=self.quit)
        selectionMenu.add_command(label="Create", command=self.quit)
        selectionMenu.add_command(label="Company Printing", command=self.quit)
        selectionMenu.add_command(label="Indexing", command=self.quit)
        selectionMenu.add_command(label="Exit", command=self.quit)

        self.menubar.add_cascade(label="Selection", menu=selectionMenu)

        #--------------------------------------------------------

        masterMenu = Menu(self.menubar, tearoff=0)

        masterMenu.add_command(label="Employee",command=self.quit)
        masterMenu.add_command(label="Designation",command=self.quit)
        masterMenu.add_command(label="Department",command=self.quit)
        masterMenu.add_command(label="Branch",command=self.quit)
        masterMenu.add_command(label="Payment",command=self.quit)
        masterMenu.add_command(label="State",command=self.quit)
        masterMenu.add_command(label="Employee (Browse)",command=self.quit)
        masterMenu.add_command(label="Emolument Update",command=self.quit)
        masterMenu.add_command(label="Deduction Update",command=self.quit)
        masterMenu.add_command(label="Family Details (Employee)",command=self.quit)
        masterMenu.add_command(label="Workmen Number",command=self.quit)

        self.menubar.add_cascade(label="Master", menu=masterMenu)

        #--------------------------------------------------------

        datamaintainMenu = Menu(self.menubar, tearoff=0)
        
        attendanceMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Attendance", menu=attendanceMenu)

        manualeditMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Manual Edit", menu=manualeditMenu)

        loanAdvanceMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Loan/Advances", menu=loanAdvanceMenu)

        datamaintainMenu.add_command(label="Rewards",command=self.quit)
        datamaintainMenu.add_command(label="Increments",command=self.quit)
        datamaintainMenu.add_command(label="Training",command=self.quit)

        pfesiwagesMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="PF/ESI Wages (Direct Feeding)", menu=pfesiwagesMenu)

        incomeTaxMaintainMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Income Tax", menu=incomeTaxMaintainMenu)

        arrearMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Arrear", menu=arrearMenu)

        bonusmaintainMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Bonus", menu=bonusmaintainMenu)

        datamaintainMenu.add_command(label="List Of Holiday",command=self.quit)

        musterRollMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Muster Roll", menu=musterRollMenu)

        uploaderMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Uploader", menu=uploaderMenu)

        annualPFReturnMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Annual P.F. Return", menu=annualPFReturnMenu)

        datamaintainMenu.add_command(label="ID Card",command=self.quit)

        netpayMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Net Pay", menu=netpayMenu)

        attendanceAdjustMenu = Menu(datamaintainMenu, tearoff=0)
        datamaintainMenu.add_cascade(label="Attendance Adjust", menu=attendanceAdjustMenu)

        self.menubar.add_cascade(label="Data Maintenance", menu=datamaintainMenu)
        
        #--------------------------------------------------------

        reportsMenu = Menu(self.menubar, tearoff=0)

        monthlyReportsMenu = Menu(reportsMenu, tearoff=0)
        halfYearlyEsicMenu = Menu(reportsMenu, tearoff=0)
        AnnualPFMenu = Menu(reportsMenu, tearoff=0)
        BonusReportsMenu = Menu(reportsMenu, tearoff=0)
        FactoryActMenu = Menu(reportsMenu, tearoff=0)
        MISReportsMenu = Menu(reportsMenu, tearoff=0)
        HRReportsMenu = Menu(reportsMenu, tearoff=0)
        LoanAdvanceReportsMenu = Menu(reportsMenu, tearoff=0)
        LWFReportsMenu = Menu(reportsMenu, tearoff=0)
        MasterFilesMenu = Menu(reportsMenu, tearoff=0)
        miscPFEsicMenu = Menu(reportsMenu, tearoff=0)
        incomeTaxMenu = Menu(reportsMenu, tearoff=0)
        LeavesMenu = Menu(reportsMenu, tearoff=0)
        ContractorsMenu = Menu(reportsMenu, tearoff=0)
        exemptedPFMenu = Menu(reportsMenu, tearoff=0)
        employementExchangeMenu = Menu(reportsMenu, tearoff=0)
        gratuityMenu = Menu(reportsMenu, tearoff=0)
        statisticalMenu = Menu(reportsMenu, tearoff=0)
        miscCustomerMenu = Menu(reportsMenu, tearoff=0)

        self.menubar.add_cascade(label="Reports", menu=reportsMenu)
        reportsMenu.add_cascade(label="Monthly Reports", menu=monthlyReportsMenu)
        reportsMenu.add_cascade(label="Half yearly E.S.I.C", menu=halfYearlyEsicMenu)
        reportsMenu.add_cascade(label="Annual P.F.", menu=AnnualPFMenu)
        reportsMenu.add_cascade(label="Bonus", menu=BonusReportsMenu)
        reportsMenu.add_cascade(label="Factory Act", menu=FactoryActMenu)
        reportsMenu.add_cascade(label="M.I.S. Reports", menu=MISReportsMenu)
        reportsMenu.add_cascade(label="H.R. Reports", menu=HRReportsMenu)
        reportsMenu.add_cascade(label="Loan/Advance", menu=LoanAdvanceReportsMenu)
        reportsMenu.add_cascade(label="Labour Welfare Fund", menu=LWFReportsMenu)
        reportsMenu.add_cascade(label="Master Files", menu=MasterFilesMenu)
        reportsMenu.add_cascade(label="Misc. PF/ESI Return", menu=miscPFEsicMenu)
        reportsMenu.add_cascade(label="Income tax", menu=incomeTaxMenu)
        reportsMenu.add_cascade(label="Leaves", menu=LeavesMenu)
        reportsMenu.add_cascade(label="Contractors", menu=ContractorsMenu)
        reportsMenu.add_cascade(label="Exempted PF (Trust)", menu=exemptedPFMenu)
        reportsMenu.add_cascade(label="Employement Exchange", menu=employementExchangeMenu)
        reportsMenu.add_cascade(label="Gratuity", menu=gratuityMenu)
        reportsMenu.add_cascade(label="Statistical", menu=statisticalMenu)
        reportsMenu.add_cascade(label="Misc. Customer", menu=miscCustomerMenu)
        
        #--------------------------------------------------------

        updationMenu = Menu(self.menubar, tearoff=0)
        updationMenu.add_command(label="Month Change",command=self.quit)
        updationMenu.add_command(label="Insertion Working Day",command=self.quit)
        updationMenu.add_command(label="Calculation - Salary",command=self.quit)
        updationMenu.add_command(label="Data updation",command=self.quit)
        updationMenu.add_command(label="Data Transfer (Attendance Machine)",command=self.quit)
        updationMenu.add_command(label="Previous Salary Add in Current File",command=self.quit)
        updationMenu.add_command(label="New Employee Add in Current File",command=self.quit)
        updationMenu.add_command(label="Bonus Calculation",command=self.quit)
        updationMenu.add_command(label="Factory Act Calculation",command=self.quit)
        updationMenu.add_command(label="Master List Add in Current File",command=self.quit)
        updationMenu.add_command(label="Transfer Data to Excel",command=self.quit)
        updationMenu.add_command(label="Calculation Overtime",command=self.quit)
        self.menubar.add_cascade(label="Updation", menu=updationMenu)

        #--------------------------------------------------------

        setupMenu = Menu(self.menubar, tearoff=0)
        
        setupMenu.add_command(label="Install",command=self.quit)
        setupMenu.add_command(label="Setup Company",command=self.quit)
        setupMenu.add_command(label="Setup Allowance",command=self.quit)
        setupMenu.add_command(label="Setup Deduction",command=self.quit)
        setupMenu.add_command(label="Setup Income Tax",command=self.quit)
        setupMenu.add_command(label="Password Change",command=self.quit)
        setupMenu.add_command(label="Salary File Deletion",command=self.quit)
        setupMenu.add_command(label="Browse Files",command=self.quit)
        setupMenu.add_command(label="Command Line",command=self.quit)
        setupMenu.add_command(label="Recall Master Delete",command=self.quit)
        setupMenu.add_command(label="Invalid Subscript Reference",command=self.quit)
        setupMenu.add_command(label="Code Setting",command=self.quit)
        setupMenu.add_command(label="Previous Month Deletion",command=self.quit)
        setupMenu.add_command(label="I.Card No. Change",command=self.quit)
        setupMenu.add_command(label="Update Advance",command=self.quit)
        setupMenu.add_command(label="Update Increment",command=self.quit)
        setupMenu.add_command(label="Delete Unrecovered Advance",command=self.quit)
        setupMenu.add_command(label="Data Transfer (Servagya)",command=self.quit)
        setupMenu.add_command(label="Updated-Master",command=self.quit)
        setupMenu.add_command(label="Updated-Months Total",command=self.quit)

        self.menubar.add_cascade(label="Setup", menu=setupMenu)

        #--------------------------------------------------------

        quitMenu = Menu(self.menubar, tearoff=0)
        quitMenu.add_command(label="Quit",command=self.quit)#add a warning dialog before quitting
        quitMenu.add_command(label="About",command=lambda:info("About Vantage","Vantage Payroll is a Software Made Exclusively For\n G. P. Singh And Associates\nVersion 1.0\nDeveloped by TheHackerClown"))

        self.menubar.add_cascade(label="Quit",menu=quitMenu)

        #--------------------------------------------------------

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


    def refreshTitle(self):
        """Change the title of the main window."""
        self.wm_title("Vantage Payroll          "+self.month+"          "+self.companytitle)

    # Draw the main window content
    # Tab System to be implemented later
    def drawWindow(self):
        button = ttk.Button(self, text="Welcome to Vantage")
        button.pack(pady=20)


if __name__ == "__main__":
    vantageApp = Vantage()
    vantageApp.mainloop()