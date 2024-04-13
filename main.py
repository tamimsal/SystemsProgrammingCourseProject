#SIC assembler pass 1 
#Done By: Tamim Salhab

#to run this code you could just run it in the ide with python envirement or just write python3 main.py
#the code.asm is stored in the tests folder, if you want to run different tests you could change the code or change directory file name
#the code is stored in intermediate.mdt file in the same folder

#Conversion table to help convert from decimal to hexadecimal
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'} 
  

#Method to convert decimal value to hexadecimal value
def decimalToHexadecimal(decimal): 
    hexadecimal = '' 
    while(decimal > 0): 
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal 
        decimal = decimal // 16
    return hexadecimal 
  

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
    return result
    

SYMTAB = {}                                 #defining SYMTAB to store values
f = open("intermediate.mdt", "w")           #opening intermediate file

file1 = open('tests/code.asm', 'r')         #opening test file, you can edit the path to add new file
Lines = file1.readlines()                   #defining variabiles to store values
PROGLENGTH = 0
count = 0
PRGNAME = ""
location = 0


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
    f.write(dic[2])
writeLst = open("listingFile.lst", "w")

def writingListingFile(loca, fileToUse):
    optabFile = open("OPTAB.asm", 'r')
    opLines = optabFile.readlines()
    toLookFor = fileToUse[1]
    firstByte = ""
    for opLine in opLines:
        dicta = opLine.split(" ")
        while("" in dicta):
            dicta.remove("") 
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

    writeLst.write(wee + "      ")
    
    writeLst.write(firstByte)

    for sy in SYMTAB:
        if(wee == sy):
            writeLst.write(SYMTAB[sy])
            print(wee + " " + sy)

            

    writeLst.write("\n")





#Extracting SYMTAB and LOCCTR
for Line in Lines:
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
            location = location + 1
        else:
            leng = 3
            if count != 0:
                location = location + leng
        count+=1
        if dic[1] == "END":
            PROGLENGTH = location

        fileToUse = dic
        loca = qaa
        writingListingFile(loca, fileToUse)


for line in Lines:
    comment = ""
    for i in line [40:70]:
        comment = comment + str(i)











#Converting Program length to the right form
PROGLENGTH = decimalToHexadecimal(PROGLENGTH)
PROGLENGTH = hexTo4Hex(PROGLENGTH)



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

