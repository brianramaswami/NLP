#Brian Ramaswami
#bramaswami@zagmail.gonzaga.edu
#CPSC475
#Project2 types of substring searches.
'''
GO TO MAIN AND SELECT WHICH PROGRAM TO RUN
'''

import sys
'''
HELPER FUNCTIONS
'''
def readInFile(fileName):
    f = open(fileName, "r")
    print(f.read())

'''
OPENS FILE TO READ IN CONTENT
'''
def my_open():
    print ("This program will ask you to enter the name of an existing file.")
    print ("Be sure to put quotation marks around the file name")
    while(True):
        fin = input('Enter an input file name\n')
        try:
            fin = open(fin, 'r')
            break
        except:
            print("Invalid file name.  Try again.")
    return fin


'''
READS FILE IN AS A STRING
'''
def read_file_as_string(fin):
    string = fin.read()
    return string

'''
READS FILE IN LINE BY LINE
'''
def read_file_as_line(fin):
    for line in fin:
        print(line.rstrip('\n')) #rstrip removes '\n' from each line because
                                 #print inserts '\n'

def searchSub(string,subStr,posStr_in):
    posSub = 0;
    posStr = posStr_in
    while(posSub < len(subStr)):
        if string[posStr] == subStr[posSub]:
            posSub = posSub + 1
            posStr = posStr + 1
        else:
            return -1
    return posStr_in

def naiveSearch(string,subStr, stringCount):
    posStr = 0
    lastSub = len(string) - len(subStr)

    while (posStr <= lastSub):
        pos = searchSub(string,subStr,posStr)
        if (pos >= 0):
            #print "substring starts at " + str(pos)
            newSpot = int(str(pos)) + len(subStr)
            stringCount = stringCount + 1
            #print(string)
            string = string[newSpot: ]
            #print(string)
            #print(stringCount)
            naiveSearch(string,subStr,stringCount)
            #print(stringCount)
            break
        else:
            posStr = posStr + 1
    if posStr > lastSub:
        print ("substring not found or finished searching")
        print("final string count is : " , stringCount)
        sys.exit()


'''
'''
def program1():
    fileName = raw_input("Please enter a file name: ")
    #type(fileName);
    #readInFile(fileName)
    f = open(fileName, "r").read()
    subString = raw_input("Please enter a substring: ")
    count = f.count(subString)
    #print(f)
    print(count)
    f.close()



def program2():
    fin = my_open()
    string = read_file_as_string(fin)
    subString = input("Please enter a substring: ")
    fin.close
    stringCount = 0
    naiveSearch(string, subString, stringCount)

    
def main():
    #program1()
    program2()



main()
