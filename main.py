conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'} 
  


def decimalToHexadecimal(decimal): 
    hexadecimal = '' 
    while(decimal > 0): 
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal 
        decimal = decimal // 16
  
    return hexadecimal 
  
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
    

SYMTAB = {}
f = open("intermediate.mdt", "w")

file1 = open('code.asm', 'r')
Lines = file1.readlines()
PROGLENGTH = 0
count = 0
PRGNAME = ""
location = 0


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


for line in Lines:
    comment = ""
    for i in line [40:70]:
        comment = comment + str(i)
    


PROGLENGTH = decimalToHexadecimal(PROGLENGTH)
PROGLENGTH = hexTo4Hex(PROGLENGTH)




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

