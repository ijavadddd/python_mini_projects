##IMPORT TKINTER FOR MAKE GUI
from tkinter import *
##USE OS MODULE FOR GET FILES PATH
import os
##USE JSON FOR SAVE CONTACTS INFORMATION
import json
##THREADING RUN FUNCTIONS AFTER SECONDS
import threading

##DEFINE A SPECIAL TEMPORARY MESSAGE(WILL DISPEAR AFTER MANY SECONDS)
class MyException(Exception):
    ##IF USER ENTER MASTER NAME ERROR WILL SHOW AS A LABLE BUT IF DOESN'T ERROR WILL JUST PRINT IN TERMINAL 
    def __init__(self,message,master=None):
        self.message =str( message)
        self.master = master
        super().__init__(self.message)
        if self.master!=None:
            self.errorLabel=Label(master=self.master,text=f'{self.message}',font=('','13'),fg='red')
            self.errorLabel.pack()
            ##RUN SECOND PARAMETER(THE FUNCTION) AFTER 2 SECOND(PARAMTER 1)
            threading.Timer(2,lambda :MyException.DeleteErrorLabel(self)).start()
    ##THIS FUNCTION WILL DELETE LABLE
    def DeleteErrorLabel(self):
            self.errorLabel.pack_forget()
    def __str__(self):
        return self.message
    
##THIS CLASS MAKE CONTACTS LIST CLASS
class Contact:
    def __init__(self,contactsList,masterName):
        self.contactsList = contactsList
        self.masterName = masterName
    ##THIS CLASS MAKE CONTACTS LIST WITH ENTRY
    def ContantTable(self):
        ##DEFINE FILE PATH DIRECTIONS FOR JOIN JSON FILE PATH WITH IT
        fileDir=os.path.dirname(__file__)
        contactsData=os.path.join(fileDir,'contacts\\contacts.json')
        ##THIS FUNCTION IS FOR DELETE EACH CONTACT WE CLICK ON DELETE BUTTON
        def DeleteContact(rowNumber):
            with open(contactsData,'r+') as contactsFile:
                ##GET CONTACTS LIST
                contactsList=json.load(contactsFile)
                ##DELETE THAT CONTACT WE CLICKED ON THAT DELETE BUTTON
                del contactsList[rowNumber]
                ##CLEAR CONTACTS LIST FROM JSON FILE
                with open(contactsData,'w') as contactsFile:
                    ##SAVE NEW DATA(CONTACTS LIST WITH OUT DELETED CONTACTS) IN JSON
                    json.dump(contactsList,contactsFile,indent=4)
                    contactLabel=Label(self.masterName,text='Refresh for see changes' ,fg='red',font=('','30'))
                    contactLabel.pack()
        ##THIS FUNCTION WILL EDIT CONTACTS
        def EditContact(row):
            ##CONTACT EDIT FRAME 
            editFrame=Frame(self.masterName)
            editFrame.pack()
            editFrame.place(width=700-(700/4),height=700)
            ##EDIT CONTACT LABEL
            editLabel=Label(editFrame,text='Edit Contact',font=('','20'))
            editLabel.pack()
            editLabel.place()
            
            ##THIS FUNCTION WILL SAVE DATA IN JSON
            def SaveContact(event):
                ##GET VALUES USER HAD ENTER IN ENTRY
                firstName=str(contactFirstNameEntry.get())
                lastName=str(contactLastNameEntry.get())
                mobileNumber=str(contactMobileNumberEntry.get())
                email=str(contactEmailNumberEntry.get())
                ##SAVE CHANGED DATA IN DICTIONARIES
                newContact={'FirstName':firstName,'LastName':lastName,'MobileNumber':mobileNumber,'Email':email}
                ##IF FILE DOESNE'T EXIST CAN'T OPEN WITH 'r' MODE → FILE NOT EXIST AND OPEN WITH 'w' MODE IN EXCEPT
                try:
                    ##GET OLDEST CONTACTS , IF DON'T USE THIS BLOCK WE WILL LOSE CONTACT LIST
                    with open(contactsData,'r+') as contactsFile:
                        contactsList=json.load(contactsFile)
                        ##WHY ROW-1?? BEACUSE FIRST ROW IS COLUMN NAME
                        del contactsList[row-1]
                        contactsList.append(newContact)
                    try:
                        if newContact['FirstName']=="" and newContact['LastName']=="":
                            raise MyException("Fill first name or last name,both can't be null",editFrame)
                    except MyException as error:
                        print(error)
                    else:
                        ##IF NO ERROR ACURRD SAVE CHANGES
                        with open(contactsData,'w') as contactsFile:
                            json.dump(contactsList,contactsFile,indent=4)
                        successfulyAdded=Label(master=editFrame,text='Contact Successfully Added',fg='green',font=('','12'))
                        successfulyAdded.pack()
                        successfulyAdded.place(x=20,y=380)
                        def DispeareLabel():
                            successfulyAdded.config(text='')
                        ##RUN TOP FUNCTION AFTER 2 SECOND
                        threading.Timer(2,DispeareLabel).start()
                    
                except :
                    ##IF CONTACT FILE DOESN'T EXIST MAKE IT AND SAVE CHANGES
                    with open(contactsData,'w') as contactsFile:
                        contactsList=[newContact]
                        json.dump(contactsList,contactsFile,indent=4)

            ##FIRST NAME LABEL
            contactFirstNameLabel=Label(master=editFrame,text='First name : ',font=('','13'))
            contactFirstNameLabel.pack()
            contactFirstNameLabel.place(x=20,y=102)
            ##FIRST NAME ENTRY
            contactFirstNameEntry=Entry(master=editFrame,font=('','12'))
            contactFirstNameEntry.pack()
            contactFirstNameEntry.place(x=180,y=100,width=200,height=30)
            contactFirstNameEntry.insert(END,self.contactsList[row]['FirstName'])
            ##LAST NAME LABEL
            contactLastNameLabel=Label(master=editFrame,text='Last name : ',font=('','13'))
            contactLastNameLabel.pack()
            contactLastNameLabel.place(x=20,y=152)
            ##LAST NAME ENTRY
            contactLastNameEntry=Entry(master=editFrame,font=('','12'))
            contactLastNameEntry.pack()
            contactLastNameEntry.place(x=180,y=150,width=200,height=30)
            contactLastNameEntry.insert(END,self.contactsList[row]['LastName'])
            ##MOBILE NUMBER LABEL
            contactMobileNumberLabel=Label(master=editFrame,text='Mobile number : ',font=('','13'))
            contactMobileNumberLabel.pack()
            contactMobileNumberLabel.place(x=20,y=202)
            ##MOBILE NUMBER ENTRY
            contactMobileNumberEntry=Entry(master=editFrame,font=('','12'))
            contactMobileNumberEntry.pack()
            contactMobileNumberEntry.place(x=180,y=200,width=200,height=30)
            contactMobileNumberEntry.insert(END,self.contactsList[row]['MobileNumber'])
            ##EMAIL LABEL
            contactEmailNumberLabel=Label(master=editFrame,text='Email : ',font=('','13'))
            contactEmailNumberLabel.pack()
            contactEmailNumberLabel.place(x=20,y=252)
            ##EMAIL ENTRY
            contactEmailNumberEntry=Entry(master=editFrame,font=('','12'))
            contactEmailNumberEntry.pack()
            contactEmailNumberEntry.place(x=180,y=250,width=200,height=30)
            contactEmailNumberEntry.insert(END,self.contactsList[row]['Email'])
            ##UPDATE CHANGES BUTTON
            saveContactButton=Button(master=editFrame,font=('','18'),text='Update',bg='#ff8c00',fg='#fff',cursor='hand2')
            saveContactButton.pack()
            saveContactButton.place(x=100,y=320,width=300,height=45)
            saveContactButton.bind('<Button>',SaveContact)

        ##SHOW CONTACTS LABEL
        contactLabel=Label(self.masterName,text='Contacts',font=('','30'))
        contactLabel.pack()
        contactLabel.place(y=10)
        ##CONTACTS LIST TABLE
        tableFrame=Frame(self.masterName)
        tableFrame.pack()
        ##IF NUMBER OF RECORDS WAS MORE THAN 28 , WILL ADD NewHeight 
        newHeight=600
        tableFrame.place(width=700-700/4,height=newHeight,y=100)
        ##FOR EACH CONTACT IN CONTACT LIST
        for row in range(len(self.contactsList)):
            mystr = StringVar()
            mystr.set(self.contactsList[row]["FirstName"])
            firstNameLabel=Entry(master=tableFrame,width=13,state=DISABLED,textvariable=mystr,font=('','10'))
            firstNameLabel.grid(row=row,column=0)

            mystr = StringVar()
            mystr.set(self.contactsList[row]["LastName"])
            lastNameLabel=Entry(master=tableFrame,width=12,state=DISABLED,textvariable=mystr,font=('','10'))
            lastNameLabel.grid(row=row,column=1)

            mystr = StringVar()
            mystr.set(self.contactsList[row]["MobileNumber"])
            mobileNumberLabel=Entry(master=tableFrame,width=15,state=DISABLED,textvariable=mystr,font=('','10'))
            mobileNumberLabel.grid(row=row,column=2)

            mystr = StringVar()
            mystr.set(self.contactsList[row]["Email"])
            emailLabel=Entry(master=tableFrame,width=15,state=DISABLED,textvariable=mystr,font=('','10'))
            emailLabel.grid(row=row,column=3)
            ##IF IT WAS ROW ONE (ROWS INCLUDE COLUMNS NAME)
            if row==0:
                mystr = StringVar()
                mystr.set('Delete?')
                deleteLabel=Entry(master=tableFrame,width=9,state=DISABLED,textvariable=mystr,font=('','10'))
                deleteLabel.grid(row=row,column=4)

                mystr = StringVar()
                mystr.set('Edit?')
                editLabel=Entry(master=tableFrame,width=5,state=DISABLED,textvariable=mystr,font=('','10'))
                editLabel.grid(row=row,column=5)

            else:
                mystr = StringVar()
                mystr.set('Delete')
                deleteLabel=Entry(master=tableFrame,width=9,cursor='hand2',state=DISABLED,textvariable=mystr,font=('','10'))
                deleteLabel.grid(row=row,column=4)
                deleteLabel.bind('<Button>',lambda event,rowNumber=row:DeleteContact(rowNumber-1))
                
                mystr = StringVar()
                mystr.set('Edit')
                editLabel=Entry(master=tableFrame,width=5,cursor='hand2',state=DISABLED,textvariable=mystr,font=('','10'))
                editLabel.grid(row=row,column=5)
                editLabel.bind('<Button>',lambda event,rowNumber=row:EditContact(rowNumber))
            if row>27:
                newHeight+=30
                tableFrame.place(height=newHeight)
        return newHeight