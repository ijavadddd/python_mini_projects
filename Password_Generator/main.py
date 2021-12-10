import random
import string
import datetime
import json
import os

class Password:
    ##DEFINE LISTS CONTAIN CHARACTERS
    lowerCaseList = string.ascii_lowercase
    upperCaseList = string.ascii_uppercase
    digitList = string.digits
    punctuationList = '!$#@&*_-=+%^~'
    
    
    ##THIS FUNCTION WILL SAVE ALL GENERATED PASSWORD WITH DATE IN JSON
    @staticmethod
    def __SaveInJson(password):
        filePath='MyPass/passwords.json'
        savedPassFile=os.path.exists(filePath)
        if savedPassFile:
            openFileMode='r+'
        else:
            openFileMode='w'
        with open(filePath,openFileMode) as passFile:
            passwords=[]
            inSecond=datetime.datetime.now()
            inSecond=str(inSecond)
            fileSize=os.path.getsize(filePath)
            if openFileMode=='r+' and fileSize!=0:
                passwords.append(json.load(passFile))
                passwords.append([{f'{inSecond}':f'{password}'}])
                passwords=[j for i in passwords for j in i]
            else:
                passwords=[{f'{inSecond}':f'{password}'}]
            with open(filePath,openFileMode) as writePass:
                    json.dump(passwords,writePass,indent=4)
    
    ##FUNCTION FOR ENTER EACH CHARACTER NUMBER
    @staticmethod
    def SpecialNumber(lowerCase=0,upperCase=0,digit=0,punctuation=0):
        lowerCase = lowerCase
        upperCase = upperCase
        digit = digit
        punctuation = punctuation
        passwordList=[random.choice(i[0]) for i in ((Password.lowerCaseList,lowerCase) , (Password.upperCaseList , upperCase) , (Password.digitList, digit) , (Password.punctuationList , punctuation)) for j in range(0,i[1])]
        characterNumber=lowerCase + upperCase + digit + punctuation
        password=random.sample(passwordList,k=characterNumber)
        password=''.join(password)
        Password.__SaveInJson(password)
        return password
    
    ##FUNCTION FOR ENTER TOTAL CHARACTER NUMBER
    @staticmethod
    def AllCharacter(allCharacter=0):
        allCharacter = allCharacter
        if allCharacter==0:
                allCharacter=12
                passwordList=[random.choice(i) for i in (Password.lowerCaseList , Password.upperCaseList , Password.digitList , Password.punctuationList) for j in range(0,(allCharacter)//4)]
                password=random.sample(passwordList,k=allCharacter)
                password=''.join(password)
                return password
        else:
            passwordList=[random.choice(i) for i in (Password.lowerCaseList , Password.upperCaseList , Password.digitList , Password.punctuationList) for j in range(0,(allCharacter)//4)]
            if len(passwordList) < allCharacter:
                remainingCharacter = allCharacter%4
                for i in range(0,remainingCharacter):
                    for j in (Password.lowerCaseList , Password.upperCaseList , Password.digitList , Password.punctuationList):
                        passwordList.append(random.choice(j))
                        continue
            password=random.sample(passwordList,k=allCharacter)
            password=''.join(password)
            Password.__SaveInJson(password)
            return password