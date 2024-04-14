#SIC assembler pass1 and pass2
#Done By: Tamim Salhab

#to run this code you could just run it in the ide with python envirement or just write python3 main.py
#the code.asm is stored in the tests folder, if you want to run different tests you could change the code or change directory file name
#you and test error handling by changing the file name, all expected error the program is able to handle them and react accordingly 

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

#Replacer method is used to replace string chars by index
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

#hexToDecimal method is used to convert numbers from hex notation to decimal notation
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
    
#Method to convert from hexadecimal to 6-bit hexadecimal value
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

#Method to do nothing!
def doNothing():
    doNothing = True

#Method to write on listing file
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

    #handling opcode errors
    if(fileToUse[1] not in operands and fileToUse[1] != "START" and fileToUse[1] != "BYTE" and fileToUse[1] != "WORD" and fileToUse[1] != "RESW" and fileToUse[1] != "RESB" and fileToUse[1] != "END"):
        print("Error! opcode " + fileToUse[1] +" not avaliable")
        exit()
    
    larerals = list(SYMTAB.keys())
    toCompare = fileToUse[2].replace("\n","")
    toCompare = toCompare.replace(",X","")

    #handling laterals errors
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


#Method to check symbol errors
def checkSymbolErrors():
    # Dictionary to count occurrences of symbols
    countSym = {}

    # Loop through each line starting from the second line
    for line in Lines[1:]:
        # Split the line by spaces
        dic = line.split(" ")
        # Initialize count for each symbol to 0
        countSym[dic[0]] = 0

    # Loop through each line again
    for line in Lines[1:]:
        # Split the line by spaces
        dic = line.split(" ")
        
        # Check if the first element is alphabetic (a symbol)
        if(dic[0].isalpha()):
            # Increment the count for the symbol
            countSym[dic[0]] += 1
        
        # Check if the first element is a period (indicating end of line)
        if(dic[0] == "."):
            # Clear the dictionary
            dic.clear()
        
        # Remove any empty strings from the list
        while("" in dic):
            dic.remove("") 

    # Check for duplicate symbols
    for z in countSym:
        if countSym[z] > 1:
            # Print error message and exit if duplicate symbols found
            print("Error! no duplicate symbols are allowed")
            print(z + " symbol is already in use")
            exit()

startingNew = False
# Loop through each line in the input file
for Line in Lines:
    if startingNew == False:
        # Split the line by spaces and extract the location
        dic = Line.split(" ")
        location = dic[-1]
        location = hexToDecimal(location)
        startingNew = True
 
    # Check if the line is not a comment line
    if(Line[0] != '.'):
        # Split the line by spaces and remove any empty strings
        dic = Line.split(" ")
        dic[0].replace(" ", "")
        
        # If program name is not yet set, set it
        if(PRGNAME == ""):
            PRGNAME = dic[0]
        
        # Add the label to SYMTAB if it's not already there
        if(dic[0]):
            SYMTAB[dic[0]] = 0
        
        while("" in dic):
            dic.remove("")   
        
        # If label is not present, insert an empty string
        if str(dic[0]) not in SYMTAB.keys():
            dic.insert(0,"")
        
        # Convert location to hexadecimal and add to SYMTAB
        wrwr = decimalToHexadecimal(location)
        qaa = hexTo4Hex(wrwr)
        
        # Update SYMTAB with the label and its location
        if(dic[0] != ""):
            SYMTAB[dic[0]] = qaa

        # Write to intermediate file
        writingOnIntermidiateFile(qaa,dic)
        
        # Update location based on operation code
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
        # Update program length if END statement is encountered
        if dic[1] == "END":
            PROGLENGTH = location
    else:
        # Write comment lines to the output file
        f.write(Line)

# Initialize variables
startingAdd = 0
startingNew = False
startingNewTwo = False

# Loop through each line in the input file
for Line in Lines:
    # If startingNew is False, extract the starting address from the first line
    if startingNew == False:
        dic = Line.split(" ")
        location = dic[-1]
        startingAdd = location
        location = hexToDecimal(location)
        startingNew = True
    
    # Check if the line is not a comment line
    if(Line[0] != '.'):
        # Split the line by spaces and remove any empty strings
        dic = Line.split(" ")
        dic[0].replace(" ", "")
        while("" in dic):
            dic.remove("")   
        
        # If label is not present, insert an empty string
        if str(dic[0]) not in SYMTAB.keys():
            dic.insert(0,"")
        
        # Convert location to hexadecimal and write to listing file
        wrwr = decimalToHexadecimal(location)
        qaa = hexTo4Hex(wrwr)
        fileToUse = dic
        writingListingFile(qaa, fileToUse)
        
        # Update location based on operation code
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

        count += 1
        
        # If startingNewTwo is False, adjust the location for the starting address
        if startingNewTwo == False:
            location = location - 3
            startingNewTwo = True

for line in Lines:
    comment = ""
    for i in line [40:70]:
        comment = comment + str(i)

def writingOnObjectFile():
    # Open the object file for writing
    objectFile = open("objectFile.obj", 'w')
    
    # Write the header record
    objectFile.write('H^' + PRGNAME)
    prgNameLen = len(PRGNAME)
    
    # Pad the program name field with spaces if less than 6 characters
    while prgNameLen < 6:
        objectFile.write(" ")
        prgNameLen += 1
    
    # Write the program starting address and program length
    objectFile.write("^00" + startingAdd[0] + startingAdd[1] + startingAdd[2] + startingAdd[3] + "^00" + PROGLENGTH + "\n")
    
    # Initialize variables for writing text records
    toWrite = ""
    recLength = 0
    prevLoc = 0
    isFirstOne = False
    isToprint = False
    
    # Loop through each record in OBJDIC
    for rec in OBJDIC:
        # Calculate the current location
        if(prevLoc != 0):
            nowLoc = hexToDecimal(rec)
            # Check if there's a gap of more than 3 between current and previous locations
            if(nowLoc - prevLoc > 3):
                lengthOfrecord = decimalToHexadecimal(recLength)
                toWrite = replacer(toWrite,lengthOfrecord[0],9)
                toWrite = replacer(toWrite,lengthOfrecord[1],10)
                objectFile.write(toWrite + "\n")
                recLength = 0
            prevLoc = hexToDecimal(rec)
        
        # Set the previous location if it's the first record
        if(isFirstOne == False):
            prevLoc = hexToDecimal(rec)
            isFirstOne = True
        
        # Check if adding the current record would exceed the text record length
        if(recLength + 3 > 30):
            isToprint = True
        
        # Handle different scenarios for creating text records
        if(recLength == 0):
            toWrite = "T^"
            toWrite = toWrite + "00" + rec + "^##^" + OBJDIC[rec]
            if(len(OBJDIC[rec]) == 2):
                recLength += 1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength += 3  
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
                recLength += 1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength += 3
        else:
            if(len(OBJDIC[rec]) > 0):
                toWrite = toWrite + "^" + OBJDIC[rec]
            if(len(OBJDIC[rec]) == 2):
                recLength += 1
            elif(len(OBJDIC[rec]) == 6 or len(OBJDIC[rec]) == 3):
                recLength += 3
    
    # Write the last text record
    lengthOfrecord = decimalToHexadecimal(recLength)
    if(len(lengthOfrecord) == 1):
        lengthOfrecord = "0" +  lengthOfrecord
    toWrite = replacer(toWrite,lengthOfrecord[0],9)
    toWrite = replacer(toWrite,lengthOfrecord[1],10)
    objectFile.write(toWrite + "\n")
    
    # Write the end record
    objectFile.write("E^00" + startingAdd + "\n")

#Converting Program length to the right form
startAddresssDec = hexToDecimal(startingAdd)
PROGLENGTH = PROGLENGTH - startAddresssDec - 3
PROGLENGTH = decimalToHexadecimal(PROGLENGTH)
PROGLENGTH = hexTo4Hex(PROGLENGTH)
checkSymbolErrors()
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

