from tkinter import *
import os
from tkcalendar import *
import datetime

def ShowCalendar(event):
    year=int(yearEntry.get())
    month=int(monthEntry.get())
    day=int(dayEntry.get())
    thisYearCalendar=Calendar(bodyFrame,selectmode='day',year=year,month=month,day=day)
    thisYearCalendar.pack(expand=True)
    thisYearCalendar.place(width=bodyWidth,height=400)
    calendarLable.config(text=f'{thisYearCalendar.get_date()}')



root=Tk()
width=1000
height=400
root.geometry(f'{width}x{height}')
root.title('Calnedar')
fileDir=os.path.dirname(__file__)
iconDir=os.path.join(fileDir, 'img\\calendar_icon.ico')
root.iconbitmap(iconDir)
root.resizable(False,False)

sidebarFrame=Frame(master=root,bg='#d6d6d6')
sidebarFrame.pack()
sidebarFrameWidth=width/4
sidebarFrame.place(height=height,width=width/4)

sidebarLableFrame=Frame(master=sidebarFrame,bg='red')
sidebarLableFrame.pack()
sidebarLableFrame.place(width=sidebarFrameWidth,height=50)

sidebarLable=Label(master=sidebarLableFrame,bg='red',fg='#fff',text='Calendar',font=('','20'))
sidebarLable.pack()
sidebarLable.place(width=sidebarFrameWidth,y=7)

menuItemsFrame=Frame(master=sidebarFrame,bg='#d6d6d6')
menuItemsFrame.pack()
menuItemsFrame.place(width=sidebarFrameWidth,height=300,y=50)


# DateConvertLabel=Label(master=menuItemsFrame,text='Convert date',font=('','13'),bg='#d6d6d6',fg='#000')
# DateConvertLabel.pack()
# DateConvertLabel.place(y=10)

goToLabel=Label(master=menuItemsFrame,text='Go to :',font=('','17'),bg='#d6d6d6',fg='#000')
goToLabel.pack()
goToLabel.place(y=42)

yearLabel=Label(master=menuItemsFrame,text='Year :',font=('','13'),bg='#d6d6d6',fg='#000')
yearLabel.pack()
yearLabel.place(y=82)
yearEntry=Entry(master=menuItemsFrame,font=('','14'))
yearEntry.pack()
yearEntry.place(y=80,x=65,width=sidebarFrameWidth-80,height=30)

monthLabel=Label(master=menuItemsFrame,text='Month :',font=('','13'),bg='#d6d6d6',fg='#000')
monthLabel.pack()
monthLabel.place(y=122)
monthEntry=Entry(master=menuItemsFrame,font=('','14'))
monthEntry.pack()
monthEntry.place(y=120,x=65,width=sidebarFrameWidth-80,height=30)

dayLabel=Label(master=menuItemsFrame,text='Day :',font=('','13'),bg='#d6d6d6',fg='#000')
dayLabel.pack()
dayLabel.place(y=162)
dayEntry=Entry(master=menuItemsFrame,font=('','14'))
dayEntry.pack()
dayEntry.place(y=160,x=65,width=sidebarFrameWidth-80,height=30)

goToButton=Button(master=menuItemsFrame,text='Show',font=('','14'),bg='#e00922',fg='#fff')
goToButton.pack()
goToButton.place(y=210,width=sidebarFrameWidth,height=40)
goToButton.bind('<Button>',ShowCalendar)

programmerFrame=Frame(master=sidebarFrame)
programmerFrame.pack()
programmerFrame.place(width=sidebarFrameWidth,height=100,y=300)

programmerLabel=Label(master=programmerFrame,text='Created by : ijavadddd',font=('','16'),fg='green')
programmerLabel.pack()
programmerLabel.place(y=20)

bodyFrame=Frame(master=root)
bodyFrame.pack()
bodyWidth=width-(sidebarFrameWidth)
bodyFrame.place(height=height,width=bodyWidth,x=sidebarFrameWidth)

now=datetime.datetime.now()
thisYearCalendar=Calendar(bodyFrame,year=now.year,month=now.month,day=now.day)
thisYearCalendar.pack(expand=True)
thisYearCalendar.place(width=bodyWidth,height=400)

calendarLable=Label(master=bodyFrame,text=f'{thisYearCalendar.get_date()}')
calendarLable.pack(expand=True)
calendarLable.place(width=bodyWidth)


root.mainloop()
