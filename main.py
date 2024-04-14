#SIC assembler
#Done By: Tamim Salhab

#to run this code you could just run it in the ide with python envirement or just write python3 main.py
#the code.asm is stored in the tests folder, if you want to run different tests you could change the code or change directory file name
#the code is stored in intermediate.mdt file in the same folder


  

#Method to convert decimal value to hexadecimal value
def decimalToHexadecimal(decimal):
    #Conversion table to help convert from decimal to hexadecimal
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'}  
    hexadecimal = '' 
    while(decimal > 0): 
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal 
        decimal = decimal // 16
    return hexadecimal 
  
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def hexToDecimal(hexadecimal):
    hexadecimal = "" + hexadecimal[0] + hexadecimal[1] + hexadecimal[2] + hexadecimal[3]  
    table = {'0': 0, '1': 1, '2': 2, '3': 3,  
         '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, 'A': 10, 'B': 11,  
         'C': 12, 'D': 13, 'E': 14, 'F': 15} 
  
    res = 0
  
    size = len(hexadecimal) - 1
  
    for num in hexadecimal: 
        res = res + table[num]*16**size 
        size = size - 1
    
    return res


#Method to convert from hexadecimal to 4-bit hexadecimal value
def hexTo4Hex(hexBefore):
    x = str(hexBefore)
    len = x.__len__()
    result = "" 
    if len == 0:
        result = "0000"
    elif len == 1:
        result = "000" + str(hexBefore)
    elif len == 2:
        result = "00" + str(hexBefore)
    elif len == 3:
        result = "0" + str(hexBefore)
    else:
        result = str(hexBefore)
    return result
    

def hexTo6Hex(hexBefore):
    x = str(hexBefore)
    len = x.__len__()
    result = "" 
    if len == 0:
        result = "000000"
    elif len == 1:
        result = "00000" + str(hexBefore)
    elif len == 2:
        result = "0000" + str(hexBefore)
    elif len == 3:
        result = "000" + str(hexBefore)
    elif len == 4:
        result = "00" + str(hexBefore)
    elif len == 5:
        result = "0" + str(hexBefore)
    elif len == 6:
        result = str(hexBefore)
    return result

SYMTAB = {}                                 #defining SYMTAB to store values
f = open("intermediate.mdt", "w")           #opening intermediate file

file1 = open('tests/code.asm', 'r')         #opening test file, you can edit the path to add new file
Lines = file1.readlines()                   #defining variabiles to store values
PROGLENGTH = 0
count = 0
PRGNAME = ""
location = 0
OBJDIC = {}

#Method to write intermidiate file 
def writingOnIntermidiateFile(LOCCTR, LINEIN):
    f.write(LOCCTR)
    f.write("    " + dic[0])
    lens = str(dic[0])
    le = 0
    for i in lens:
        if(i.isalpha()):
            le+=1
    le = 11 - le
    while(le > 0):
        f.write(" ")
        le-=1
    f.write(dic[1])

    lens = str(dic[1])
    le = 0
    for i in lens:
        if(i.isalpha()):
            le+=1
    le = 11 - le
    while(le > 0):
        f.write(" ")
        le-=1
    stringToUse = dic[2].removesuffix("\n")
    f.write(stringToUse + "\n")
    

writeLst = open("listingFile.lst", "w")

  
def doNothing():
    doNothing = True


def writingListingFile(loca, fileToUse):
    operands = []
    larerals = []
    optabFile = open("OPTAB.asm", 'r')
    opLines = optabFile.readlines()
    toLookFor = fileToUse[1]
    firstByte = ""
    for opLine in opLines:
        dicta = opLine.split(" ")
        while("" in dicta):
            dicta.remove("") 
        
        operands.append(dicta[0])
        if(dicta[0] == toLookFor):
            firstByte = dicta[1]
    


    writeLst.write(loca)
    writeLst.write("    " + fileToUse[0])
    lens = str(fileToUse[0])
    le = 0
    for i in lens:
        if(i.isalpha()):
            le+=1
    le = 11 - le
    while(le > 0):
        writeLst.write(" ")
        le-=1
    writeLst.write(fileToUse[1])

    lens = str(fileToUse[1])
    le = 0
    for i in lens:
        if(i.isalpha()):
            le+=1
    le = 11 - le
    while(le > 0):
        writeLst.write(" ")
        le-=1
    wee = fileToUse[2]
    wee = wee.strip()

    writeLst.write(wee)

    le = 0
    for i in wee:
        if(i.isalpha() or i == "'" or i == ',' or i.isnumeric()):
            le+=1
    le = 15 - le
    while(le > 0):
        writeLst.write(" ")
        le-=1

    if(fileToUse[1] not in operands and fileToUse[1] != "START" and fileToUse[1] != "BYTE" and fileToUse[1] != "WORD" and fileToUse[1] != "RESW" and fileToUse[1] != "RESB" and fileToUse[1] != "END"):
        print("Error! opcode " + fileToUse[1] +" not avaliable")
        exit()
    
    larerals = list(SYMTAB.keys())
    toCompare = fileToUse[2].replace("\n","")
    toCompare = toCompare.replace(",X","")



    if len(toCompare) > 0 and toCompare not in larerals and toCompare[0].isnumeric() == False:
        if toCompare[0] == 'C' and toCompare[1] == "'" and toCompare[5] == "'":
            doNothing()
        elif toCompare[0] == 'X' and toCompare[1] == "'" and toCompare[4] == "'":
            doNothing()
        else:
            print("Erorr! Invalid Lateral!")
            print(toCompare + " is invalid Lateral")
            exit()

    writeLst.write(firstByte)
    secondByte = ""
    for sy in SYMTAB:
        if sy in wee:
            secondByte = SYMTAB[sy]
    
    if(fileToUse[1] == "RSUB"):
        secondByte = "0000"
    elif(fileToUse[1] == "WORD"):
        num = int(fileToUse[2])
        if(num == 0):
            secondByte = "000000"
        else:
            num = decimalToHexadecimal(num)
            secondByte = hexTo6Hex(num)
    elif(fileToUse[1] == "END"):
        secondByte = ""
    elif(fileToUse[1] == "BYTE"):
        if(fileToUse[2][0] == 'X'):
            secondByte = "" + fileToUse[2][2] + fileToUse[2][3]
        else:
            convertToAscii = ''
            convertToAscii = fileToUse[2][2]
            convertToAscii = ord(convertToAscii)
            convertToAscii = decimalToHexadecimal(convertToAscii)
            firstByte = convertToAscii
            writeLst.write(firstByte)

            convertToAscii = ''
            convertToAscii = fileToUse[2][3]
            convertToAscii = ord(convertToAscii)
            convertToAscii = decimalToHexadecimal(convertToAscii)
            secondByte = convertToAscii

            convertToAscii = ''
            convertToAscii = fileToUse[2][4]
            convertToAscii = ord(convertToAscii)
            convertToAscii = decimalToHexadecimal(convertToAscii)
            secondByte = secondByte + convertToAscii

    writeLst.write(secondByte)
    writeLst.write("\n")
    fullBytes = firstByte + secondByte
    OBJDIC[str(loca)] = str(fullBytes)

def checkErrors():
    countSym = {}
    for line in Lines[1:]:
        dic = line.split(" ")
        countSym[dic[0]] = 0

    for line in Lines[1:]:
        dic = line.split(" ")
        if(dic[0].isalpha()):
            countSym[dic[0]]+=1
        if(dic[0] == "."):
            dic.clear()
        while("" in dic):
            dic.remove("") 
        

    for z in countSym:
        if countSym[z] > 1:
            print("Error! no duplicate symbols are allowed")
            print( z + " symbol is already in use")
            exit()
    



startingNew = False

#Extracting SYMTAB and LOCCTR
for Line in Lines:
    if startingNew == False:
        dic = Line.split(" ")
        location = dic[-1]
        location = hexToDecimal(location)
        startingNew = True
 
    if(Line[0] != '.'):
        dic = Line.split(" ")
        dic[0].replace(" ", "")
    
        if(PRGNAME == ""):
            PRGNAME = dic[0]
    
        if(dic[0]):
            SYMTAB[dic[0]] = 0
    
        while("" in dic):
            dic.remove("")   
        if str(dic[0]) not in SYMTAB.keys():
            dic.insert(0,"")
        wrwr = decimalToHexadecimal(location)
        qaa = hexTo4Hex(wrwr)
        
        if(dic[0] != ""):
            SYMTAB[dic[0]] = qaa

        writingOnIntermidiateFile(qaa,dic)
        
        if dic[1] == "RESW":
            leng = int(dic[2])
            location = location + leng*3
        elif dic[1] == "RESB":
            leng = int(dic[2])
            location = location + leng
        elif dic[1] == "BYTE":
            if(dic[2][0] == 'C'):
                location = location + 3
            else:
                location = location + 1

        else:
            leng = 3
            if count != 0:
                location = location + leng
        count+=1
        if dic[1] == "END":
            PROGLENGTH = location
    else:
        f.write(Line)




startingAdd = 0
startingNew = False
startingNewTwo = False
for Line in Lines:
    if startingNew == False:
        dic = Line.split(" ")
        location = dic[-1]
        startingAdd = location
        location = hexToDecimal(location)
        startingNew = True
        
    
    if(Line[0] != '.'):
        dic = Line.split(" ")
        dic[0].replace(" ", "")
        while("" in dic):
            dic.remove("")   
        if str(dic[0]) not in SYMTAB.keys():
            dic.insert(0,"")
        wrwr = decimalToHexadecimal(location)
        qaa = hexTo4Hex(wrwr)
        fileToUse = dic
        writingListingFile(qaa, fileToUse)
        
        if dic[1] == "RESW":
            leng = int(dic[2])
            location = location + leng*3
        elif dic[1] == "RESB":
            leng = int(dic[2])
            location = location + leng
        elif dic[1] == "BYTE":
            if(dic[2][0] == 'C'):
                location = location + 3
            else:
                location = location + 1
        else:
            leng = 3
            if count != 0:
                location = location + leng

        count+=1
        if startingNewTwo == False:
            location = location - 3
            startingNewTwo = True





for line in Lines:
    comment = ""
    for i in line [40:70]:
        comment = comment + str(i)


def writingOnObjectFile():
    objectFile = open("objectFile.obj", 'w')

    objectFile.write('H^' + PRGNAME)

    prgNameLen = len(PRGNAME)
    while prgNameLen < 6:
        objectFile.write(" ")
        prgNameLen+=1
    objectFile.write("^00" + startingAdd[0] + startingAdd[1] + startingAdd[2] + startingAdd[3] + "^00" + PROGLENGTH + "\n")
    toWrite = ""
    recLength = 0
    prevLoc = 0
    isFirstOne = False
    isToprint = False
    for rec in OBJDIC:
        if(prevLoc != 0):
            nowLoc = hexToDecimal(rec)
            if(nowLoc - prevLoc > 3):
                lengthOfrecord = decimalToHexadecimal(recLength)
                toWrite = replacer(toWrite,lengthOfrecord[0],9)
                toWrite = replacer(toWrite,lengthOfrecord[1],10)
                objectFile.write(toWrite + "\n")
                recLength = 0
            prevLoc = hexToDecimal(rec)
        
        if(isFirstOne == False):
            prevLoc = hexToDecimal(rec)
            isFirstOne = True
        if(recLength + 3 > 30):
            isToprint = True
        if(recLength == 0):
            toWrite = "T^"
            toWrite = toWrite + "00" + rec + "^##^" + OBJDIC[rec]
            if(len(OBJDIC[rec]) == 2):
                recLength+=1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength+=3
            
        elif(recLength == 30 or isToprint):
            lengthOfrecord = decimalToHexadecimal(recLength)
            toWrite = replacer(toWrite,lengthOfrecord[0],9)
            toWrite = replacer(toWrite,lengthOfrecord[1],10)
            isToprint = False
            objectFile.write(toWrite + "\n")
            recLength = 0
            toWrite = "T^"
            toWrite = toWrite + "00" + rec + "^##"
            if(len(OBJDIC[rec]) > 0):
                toWrite = toWrite + "^" + OBJDIC[rec]
            if(len(OBJDIC[rec]) == 2):
                recLength+=1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength+=3
        
        else:
            if(len(OBJDIC[rec]) > 0):
                toWrite = toWrite + "^" + OBJDIC[rec]
            if(len(OBJDIC[rec]) == 2):
                recLength+=1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength+=3
            
    lengthOfrecord = decimalToHexadecimal(recLength)
    if(len(lengthOfrecord) == 1):
        lengthOfrecord = "0" +  lengthOfrecord
    toWrite = replacer(toWrite,lengthOfrecord[0],9)
    toWrite = replacer(toWrite,lengthOfrecord[1],10)

    objectFile.write(toWrite + "\n")

    objectFile.write("E^00" + startingAdd + "\n")
    



#Converting Program length to the right form
startAddresssDec = hexToDecimal(startingAdd)

PROGLENGTH = PROGLENGTH - startAddresssDec - 3

PROGLENGTH = decimalToHexadecimal(PROGLENGTH)

PROGLENGTH = hexTo4Hex(PROGLENGTH)
checkErrors()
writingOnObjectFile()

#Printing SYMTAB, program length, and program name on the command line
print("SYMTAB")
print("Symbol     LOCCTR")
for sy in SYMTAB:
    print(sy ,end="")
    lens = str(sy)
    le = 0
    for i in lens:
        if(i.isalpha()):
            le+=1
    le = 11 - le
    while(le > 0):
        print(" " ,end="")
        le-=1
    print(SYMTAB[sy])


print("Program Name: " + PRGNAME)
print("Program Length: " + PROGLENGTH)

