def writingListingFile():
    readIntermediateFile = open("intermediate.mdt", 'r')
    linesr = readIntermediateFile.readlines()
    for liner in linesr:
        dic = liner.split(" ")
        if(dic[5] == ""):
            dic[5] = "e"
        
        while("" in dic):
            dic.remove("")  
        print(dic)


writingListingFile()