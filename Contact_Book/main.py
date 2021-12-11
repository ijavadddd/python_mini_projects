##IMPORT TKINTER FOR MAKE GUI
from tkinter import *
##USE OS MODULE FOR GET FILES PATH
import os
##USE JSON FOR SAVE CONTACTS INFORMATION
import json
##USE THIS MODULE FOR USE APPEND LEFT 
import collections
##USE THIS MODULE FOR OPEN WEB PAGE LINKS
import webbrowser
##MY MODULE FOR SHOW CONTACTS IN TABLE AND DELETE ,EDIT ...
import ContactModule
##THREADING RUN FUNCTIONS AFTER SECONDS
import threading

##DEFINE MASTER
root=Tk()
##DEFINE WINDOW WIDTH AND HEIGHT
width=700
height=700
root.geometry(f'{width}x{height}')
##DEFINE WINDOW TITLE
root.title('Contact Book')
##GET FILE PATH DIRECTION
fileDir=os.path.dirname(__file__)
##DEFINE WINDOW ICON WITH ATTACH IMG DIRECTIO WITH FILE DIRECTIONS
iconDir=os.path.join(fileDir,'img\\contact_book.ico')
##SET WINDOW ICON
root.iconbitmap(iconDir)
##LOCK WINDOW SIZE(CAN'T RESIZE WINDOW)
root.resizable(False,False)

##DEFINE JSON FILE(THE FILE WILL SAVE CONTACTS INFO) WITH ATTACH FILE DIRECTIONS WITH JSON DIRECTION
contactsData=os.path.join(fileDir,'contacts\\contacts.json')

##THIS FUNCTIONS WILL ADD CONTACT AND SAVE IT TO CONTACT.JSON FILE
def AddContact(event):
    ##AFTER USER CLICK SAVE BUTTON DATA WILL BE SAVE IN JSON
    def SaveContact(event):
        ##GET VALUES FROM ENTRIES(INPUTS) USER TYPED 
        ##GET USER FIRST NAME FROM ENTRY 
        firstName=str(contactFirstNameEntry.get())
        ##GET USER LAST NAME FROM ENTRY 
        lastName=str(contactLastNameEntry.get())
        ##GET USER MOBILE NUMBER FROM ENTRY 
        mobileNumber=str(contactMobileNumberEntry.get())
        ##GET USER EMAIL FROM ENTRY 
        email=str(contactEmailNumberEntry.get())
        
        
        ##DEFINE NEW CONTACT DICTIONARY FOR ADD TO CONTACT LIST FOR SAVE AS JSON
        newContact={'FirstName':firstName,'LastName':lastName,'MobileNumber':mobileNumber,'Email':email}
        
        ##IF FILE DOESEN'T EXIST CAN'T OPEN IT WITH 'r+' MODE SO WILL GO TO EXCEPT AND OPEN FILE WITH 'w' MODE FOR CREATE AND WRITE IN FILE
        try:
            ##OPEN FILE WITH 'r' MODE FOR GET OLD DATA AND ADD NEW DATA(CONTACT) TO IT AND SAVE ALL DATA TO FILE
            ##IF WE OPEN FILE WITH 'w' MODE WILL LOSE OLD DATA
            with open(contactsData,'r+') as contactsFile:
                ##GET NEW DATA AS A LIST
                contactsList=json.load(contactsFile)
                ##APPEND NEW CONTACT TO OLD CONTACT LIST
                contactsList.append(newContact)
            ##IF USER NAME and last name WAS EMPTY DON'T LET USER SAVE NEW CONTACT AND SHOW ALERT IN EXCEPT
            try:
                if newContact['FirstName']=="" and newContact['LastName']=="":
                    raise ContactModule.MyException("Fill first name or last name,both can't be null",bodyFrame)
                else:
                    ##CLEAR ENTRIES(INPUTS) AFTER GET THEM DATA
                    contactFirstNameEntry.delete(0,END)
                    contactLastNameEntry.delete(0,END)
                    contactMobileNumberEntry.delete(0,END)
                    contactEmailNumberEntry.delete(0,END)
            except ContactModule.MyException as error:
                print(error)
            ##IF NO ERROR ACCURD
            else:
                ##DELETE OLD DATA AND SAVE NEW LIST CONTAIN OLD CONTACTS + NEW CONTACT
                with open(contactsData,'w') as contactsFile:
                    ##SAVE NEW LIST TO JSON 
                    json.dump(contactsList,contactsFile,indent=4)
                ##AFTER SAVE DATA WITHOUT ERROR SHOW SUCCESSFUL TEXT TO USER
                successfulyAdded=Label(master=bodyFrame,text='Contact Successfully Added',fg='green',font=('','12'))
                successfulyAdded.pack()
                successfulyAdded.place(x=20,y=390)
                ##FUNCTION FOR HIDEN SUCCESSFUL MESSAGE
                def DispeareLabel():
                    successfulyAdded.config(text='')
                ##RUN TOP FUNCTION AFTER 2 SECOND
                threading.Timer(2,DispeareLabel).start()
                
        ##IF COULD'NT OPEN FILE WITH 'r+' → IT MEAN FILE DOESN'T EXIST AND MOST OPEN WITH 'w' MODE 
        except :
            with open(contactsData,'w') as contactsFile:
                ##APPEND NEW  CONTACT DICTIONARY TO LIST AND SAVE IT TO JSON
                contactsList=[newContact]
                json.dump(contactsList,contactsFile,indent=4)

    ##DELETE WIDGETS
    bodyWelcomLable.pack_forget()
    bodyAddContactButton.pack_forget()
    
    ##DEFINE A FRAME FOR ADD CONTACTS TAB
    addContactFrame=Frame(master=bodyFrame)
    addContactFrame.pack()
    addContactFrame.place(width=bodyWidth,height=height,)
    ##DEFINE ADD NEW CONTACTS LABEL FOR HEAD OF THE PAGE(FRAME)
    addContactLabel=Label(master=addContactFrame,text='Add new contact',font=('','22'))
    ##pady MARGIN FROM TOP
    addContactLabel.pack(pady=20)
    ##FIRST NAME LABEL(FOR DEFINE WHAT WE NEED IN NEXT ENTRY)
    contactFirstNameLabel=Label(master=addContactFrame,text='First name : ',font=('','13'))
    contactFirstNameLabel.pack()
    contactFirstNameLabel.place(x=20,y=102)
    ##FIRST NAME ENTRY
    contactFirstNameEntry=Entry(master=addContactFrame,font=('','12'))
    contactFirstNameEntry.pack()
    contactFirstNameEntry.place(x=180,y=100,width=200,height=30)
    ##LAST NAME LABEL
    contactLastNameLabel=Label(master=addContactFrame,text='Last name : ',font=('','13'))
    contactLastNameLabel.pack()
    contactLastNameLabel.place(x=20,y=152)
    ##LAST NAME ENTRY
    contactLastNameEntry=Entry(master=addContactFrame,font=('','12'))
    contactLastNameEntry.pack()
    contactLastNameEntry.place(x=180,y=150,width=200,height=30)
    ##MOBILE NUMBER LABEL
    contactMobileNumberLabel=Label(master=addContactFrame,text='Mobile number : ',font=('','13'))
    contactMobileNumberLabel.pack()
    contactMobileNumberLabel.place(x=20,y=202)
    ##MOBILE NUMBER ENTRY
    contactMobileNumberEntry=Entry(master=addContactFrame,font=('','12'))
    contactMobileNumberEntry.pack()
    contactMobileNumberEntry.place(x=180,y=200,width=200,height=30)
    ##EMAIL LABEL
    contactEmailNumberLabel=Label(master=addContactFrame,text='Email : ',font=('','13'))
    contactEmailNumberLabel.pack()
    contactEmailNumberLabel.place(x=20,y=252)
    ##EMAIL ENTRY
    contactEmailNumberEntry=Entry(master=addContactFrame,font=('','12'))
    contactEmailNumberEntry.pack()
    contactEmailNumberEntry.place(x=180,y=250,width=200,height=30)
    ##GET AND SAVE DATA IN FILE BUTTON
    saveContactButton=Button(master=addContactFrame,font=('','18'),text='Save',bg='#eb4034',fg='#fff',cursor='hand2')
    saveContactButton.pack()
    saveContactButton.place(x=100,y=320,width=300,height=45)
    saveContactButton.bind('<Button>',SaveContact)


##THIS FUNCTION WILL SHOW CONTACT LIST 
def ShowContactList(event):
    ##DEFINE FRAME FOR SHOW CONTACTS TAB
    contactListFrame=Frame(master=bodyFrame)
    contactListFrame.pack()
    contactListFrame.place(width=bodyWidth,height=height)
    ##IN FEW BELOW LINE I WANT TO MAKE A SCROLLABLE FRAME FOR SHOW CONTACTS TAB FOR WHEN CONTACTS TABLE GROWS COULD SCROLL FOR SEE ALL OF THEM
    scrollCanvas = Canvas(master=contactListFrame)
    scrollCanvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = Scrollbar(contactListFrame, orient=VERTICAL, command=scrollCanvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    scrollCanvas.configure(yscrollcommand=my_scrollbar.set)
    scrollCanvas.bind('<Configure>', lambda e: scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all")))
    second_frame =Frame(scrollCanvas)                                      ## CREAT ANOTHER FRAME INSIDE CANVAS
    second_frame.pack()
    scrollCanvas.create_window((0, 0), window=second_frame,anchor="nw")        ##ADD THAT NEW FRAME TO A WINDOW IN THE CANVAS
    scrollCanvas.pack()
    ##CONFIG FRAME SIZE
    second_frame.config(width=bodyWidth,height=height)

    try:
        ##OPEN FILE INCLUDES CONTACTS LIST
        with open(contactsData,'r+') as contactsFile:
            ##GET VONTACTS LIST
            contactsList=json.load(contactsFile)
            ##IF LISTS WAS EMPTY → RAISE ERROR SHOW NO CONTACT LABEL
            if contactsList==[] or contactsList=='':
                raise Exception('list empty')
            ##MAKE OUR LIST DEQUE FOR USE APPEND LEFT
            contactsList=collections.deque(contactsList)
            ##DEFINE A DICTIONARY FOR HEAD OF THE TABLE FOR DEFINE EACH COLUMN NAME,THIS DICTIONARY WILL APPEND LEFT(APPEND IN FIRST OF CONTACTS LIST)
            contactsList.appendleft({'FirstName':'First Name','LastName':'Last Name','MobileNumber':'Mobile Number','Email':'Email'})
            ##CALL CONTACT MODULE FOR USE SHOW CONTACT TABLE FUNCTION 
            contacts=ContactModule.Contact(contactsList,second_frame)
            ##CALL SHOW CONTACT TABLE FUNCTION  AND GET NEW HEIGHT
            newHeight=contacts.ContantTable()
            # contactListFrame.config(height=newHeight)
            second_frame.config(height=newHeight)
    ##IF CAN'T OPEN FILE WITH 'r' MODE SAY YOU HAVE NO CONTACT 
    except:
        ##SHOW LABEL YOU HAVE NO CONTACT
        noContactFoundLabel=Label(master=contactListFrame,text='You have no contact',font=('','14'))
        noContactFoundLabel.pack()
        noContactFoundLabel.place(x=50,y=30)
        ##SHOW ADD CONTACT BUTTON
        addNewContactButton=Label(master=bodyFrame,text='Add new contact',font=('','12'),cursor='hand2',fg='blue')
        addNewContactButton.pack()
        addNewContactButton.place(x=228,y=32)
        addNewContactButton.bind('<Button>',AddContact)

##SHOW PROGRAMMER INFO TAB
def ShowProggramerInfo(event):
    ##FUNCTION FOR OPEN URL
    def OpenUrl(url):
        webbrowser.open_new(url)
    ##DEFINE PROGRAMMER TAB FRAME 
    programmerFrame=Frame(master=bodyFrame)
    programmerFrame.pack()
    programmerFrame.place(width=bodyWidth,height=height)
    ##PROOGRAMMER NAME LABEL
    programmerLabl=Label(master=programmerFrame,text='Created by ijavaddddd',font=('','20'))
    programmerLabl.pack()
    ##DEFINE GITHUB ICON PATH
    githubIconDir=os.path.join(fileDir,'img\\github_icon.png')
    ##DEFINE GITHUB ICON IMAGE
    githubIconImg = PhotoImage(file=githubIconDir)
    ##DEFINE GITHUB ICON IMAGE SIZE
    githubIconImg = githubIconImg.subsample(1,1)   
    ##DEFINE GITHUB ICON IMAGE AS A LABEL
    githubLabel=Label(master=programmerFrame,image=githubIconImg,cursor='hand2')
    ##DEFINE GITHUB ICON IMAGE AS A LABEL
    githubLabel.image=githubIconImg
    githubLabel.pack()
    githubLabel.place(x=10,y=50)
    githubLabel.bind('<Button>',lambda event,url='https://www.github.com/ijavadddd':OpenUrl(url))
    ##DEFINE GITHUB ICON PATH
    instagramIconDir=os.path.join(fileDir,'img\\instagram_icon.png')
    ##DEFINE GITHUB ICON IMAGE
    instagramIconImg = PhotoImage(file=instagramIconDir)
    ##DEFINE GITHUB ICON IMAGE SIZE
    instagramIconImg = instagramIconImg.subsample(3,3)   
    ##DEFINE GITHUB ICON IMAGE SIZE AS LABEL
    instagramLabel=Label(master=programmerFrame,image=instagramIconImg,cursor='hand2')
    ##DEFINE GITHUB ICON IMAGE SIZE AS LABEL
    instagramLabel.image=instagramIconImg
    instagramLabel.pack()
    instagramLabel.place(x=120,y=50)
    instagramLabel.bind('<Button>',lambda event,url='https://www.instagram.com/ijavadddd/':OpenUrl(url))


##DEFINE LEFT SIDEBAR
sidebarFrame=Frame(master=root,bg='#dedede')
sidebarFrame.pack()
sidebarWidth=width/4
sidebarFrame.place(width=sidebarWidth,height=height)
##DEFINE A SECTION(FRAME) IN SIDEBAR
sidebarMenuItemsFrame=Frame(master=root,bg='#dedede')
sidebarMenuItemsFrame.pack()
sidebarMenuItemsFrame.place(width=sidebarWidth,height=200)
##ADD CONTACT LABEL
sidebarItemAddContact=Label(master=sidebarMenuItemsFrame,text='+ Add Contact',font=('','12'),cursor='hand2',bg='#dedede',fg='#0088ff')
sidebarItemAddContact.pack()
sidebarItemAddContact.place(y=10)
sidebarItemAddContact.bind('<Button>',AddContact)
##SHOW CONTACT LIST LABEL
sidebarItemShowContactList=Label(master=sidebarMenuItemsFrame,text='Show Contact List',font=('','12'),cursor='hand2',bg='#dedede',fg='#0088ff')
sidebarItemShowContactList.pack()
sidebarItemShowContactList.place(y=50)
sidebarItemShowContactList.bind('<Button>',ShowContactList)
##PROGRAMMER LABEL
sidebarItemProgrammer=Label(master=sidebarMenuItemsFrame,text='Programmer',font=('','12'),cursor='hand2',bg='#dedede',fg='#0088ff')
sidebarItemProgrammer.pack()
sidebarItemProgrammer.place(y=90)
sidebarItemProgrammer.bind('<Button>',ShowProggramerInfo)

##DEFINE BODY FRAME
bodyFrame=Frame(master=root)
bodyFrame.pack()
bodyWidth=width-sidebarWidth
bodyFrame.place(width=bodyWidth,height=height,x=sidebarWidth)
##WELECOME LABEL
bodyWelcomLable=Label(master=bodyFrame,text='Welcome to your Contact-Book',font=('','20'))
bodyWelcomLable.pack(pady=20)
##ADD NEW CONTACT BUTTON
bodyAddContactButton=Label(master=bodyFrame,text='Add new contact',font=('','13'),cursor='hand2',fg='#0088ff')
bodyAddContactButton.pack(pady=20,padx=(0,bodyWidth-140))
bodyAddContactButton.bind('<Button>',AddContact)


root.mainloop()