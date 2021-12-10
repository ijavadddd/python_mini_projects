from tkinter import *
import os
import main

def AllCharacterGenerator(event):
    global allCharacterInput
    number=int(allCharacterInput.get())
    password=main.Password.AllCharacter(number)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    showPassword.config(text=password,font=('','13'))
    passwordCopied=Label(master=root ,text='▬ Password Copied to clipboard' ,font=('','9'),fg='green')
    passwordCopied.pack()
    passwordCopied.place(y=newy+500)


def SpecialCharacter(event):
    global upperCaseInput
    global lowerCaseInput
    global digitInput
    global punctuationInput
    lowerCase=int(lowerCaseInput.get())
    digit=int(digitInput.get())
    punctuation=int(punctuationInput.get())
    upperCase=int(upperCaseInput.get())
    password=main.Password.SpecialNumber(lowerCase,upperCase,digit,punctuation)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    showPassword.config(text=password,font=('','13'))
    passwordCopied=Label(master=root ,text='▬ Password Copied to clipboard' ,font=('','9'),fg='green')
    passwordCopied.pack()
    passwordCopied.place(y=newy+500)


filePath=os.path.dirname(os.path.abspath(__file__))
root=Tk()
root.title('Password Generator')
root.iconbitmap(f'{filePath}/images/favIcon.ico')
root.geometry('500x700')
width=500
height=700
root.resizable(False,False)


appTitle=Frame(master=root)
appTitle.pack()
appTitle.place(x=0,y=0,width=width,height=50)

Title=Label(master=appTitle,text='Password generator',font=('','20'))
Title.pack()


getCharacterFrame=Frame(master=root)
getCharacterFrame.pack()
getCharacterFrame.place(x=0,y=100,width=width,height=800)

allCharacterLabel=Label(master=getCharacterFrame ,text='Total number of characters :',font=('','14') )
allCharacterLabel.pack()
allCharacterLabel.place(y=0)
allCharacterInput=Entry(master=getCharacterFrame)
allCharacterInput.pack()
allCharacterInput.place(width=210,height=30,x=250,y=0)

allCharacterButton=Button(master=getCharacterFrame,text="Generate Password",bg='#fca503')
allCharacterButton.pack()
allCharacterButton.place(width=500,height=50,y=50)
allCharacterButton.bind('<Button>',AllCharacterGenerator)

inputsDivider=Label(master=getCharacterFrame ,text=100*'_' ,fg='#000')
inputsDivider.pack()
inputsDivider.place(y=25)

inputsDivider=Label(master=getCharacterFrame ,text='Or' ,fg='#000',font=('','20'))
inputsDivider.pack()
inputsDivider.place(width=width,y=110)

newy=150

upperCaseLabel=Label(master=getCharacterFrame ,text='Number of upperCase character:',font=('','12') )
upperCaseLabel.pack()
upperCaseLabel.place(x=0,y=newy+15)
upperCaseInput=Entry(master=getCharacterFrame)
upperCaseInput.pack()
upperCaseInput.place(width=200,height=30,x=250,y=newy+10)

lowerCaseLabel=Label(master=getCharacterFrame ,text='Number of lowerCase character:' ,font=('','12'))
lowerCaseLabel.pack()
lowerCaseLabel.place(x=0,y=newy+50)
lowerCaseInput=Entry(master=getCharacterFrame)
lowerCaseInput.pack()
lowerCaseInput.place(width=200,height=30,x=250,y=newy+50)

digitLabel=Label(master=getCharacterFrame ,text='Number of digit character:' ,font=('','12'))
digitLabel.pack()
digitLabel.place(x=0,y=newy+90)
digitInput=Entry(master=getCharacterFrame)
digitInput.pack()
digitInput.place(width=200,height=30,x=250,y=newy+90)


punctuationLabel=Label(master=getCharacterFrame ,text='Number of punctuation character:' ,font=('','12'))
punctuationLabel.pack()
punctuationLabel.place(x=0,y=newy+130)
punctuationInput=Entry(master=getCharacterFrame)
punctuationInput.pack()
punctuationInput.place(width=200,height=30,x=250,y=newy+130)

diffrentButton=Button(master=getCharacterFrame,text="Generate Password",bg='#ff0084')
diffrentButton.pack()
diffrentButton.place(width=500,height=50,y=newy+180)
diffrentButton.bind('<Button>',SpecialCharacter)

showPassword=Label(master=getCharacterFrame,text="Your Password",bg='#cccccc',font=('','18'))
showPassword.pack()
showPassword.place(width=500,height=100,y=newy+280)






root.mainloop()