import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('chester-323104-c29262154fb4.json',scope)

client = gspread.authorize(creds)

sheet = client.open("weight").sheet1
sheet2 = client.open('weight').get_worksheet(1)

#data = sheet.get_all_records()
#pprint(data)

def printRows():
    data = sheet.get_all_records()
    pprint(data)

def getLastIndex():
    fileIndex = open(r'indexes.txt','r')  
    result = ''
    list_indices =[]
    for line in fileIndex:
        s= line.split(',')
        row = int(s[0].rstrip()) 
        col = int(s[1].rstrip())
        prev_col = col
        list_indices.append([row,col])
        col=(col)%7+1
        if prev_col==7 and col ==1: row+=1
        result += f'{row},{col}'+'\n'

    fileIndex.close()
    fileIndex = open(r'indexes.txt','w')
    fileIndex.write(result)
    fileIndex.close()
    return list_indices

def getLastIndex2(name):
    fileIndex = open(r'indexes.txt','r')  
    result = ''
    content = fileIndex.readlines()
    if name == 0:
        s=content[0].split(',')
        row = int(s[0].rstrip())
        col= int(s[1].rstrip())
        prev_col = col
        prev_row=row
        col=(col)%7 +1
        if col ==1 and prev_col==7:row+=1
        result += f'{row},{col}'+'\n'
        result+=content[1]

    elif name ==1:
        s=content[1].split(',')
        row = int(s[0].rstrip())
        col= int(s[1].rstrip())
        prev_col = col
        prev_row=row
        col=(col)%7 +1           
        if col ==1 and prev_col==7:row+=1
        result+=content[0]
        result += f'{row},{col}'+'\n'
    else:
        print('Select a name')
        return

    fileIndex.close()
    fileIndex = open(r'indexes.txt','w')
    fileIndex.write(result)
    fileIndex.close()
    return (prev_row,prev_col)

def writeToCell():
    input1 = input('Enter Garrett\'s Weight: ')
    if float(input1) > 170 or float(input1)<140:
        print('Invalid weight?')
        return
    input2 = input('Enter Chester\'s Weight: ')
    input(f'Garrett weighs {input1}lbs. Chester weighs: {input2}lbs. Press any key to continue...')
    list_indices=getLastIndex()
    sheet.update_cell(list_indices[0][0],list_indices[0][1],input1)
    sheet2.update_cell(list_indices[1][0],list_indices[1][1],input2)

def entryToCell(name,weight):
    if float(weight) > 200 or float(weight)<4:
        print('Something went wrong')
        return
    list_indices = getLastIndex2(name)
    print(name)
    if name==0:
        sheet.update_cell(list_indices[0],list_indices[1],weight)
        print('Success, logged: Garrett')
    if name==1:
        sheet2.update_cell(list_indices[0],list_indices[1],weight)
        print('Success, logged: Chester')
