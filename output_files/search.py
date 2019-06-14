#!/usr/bin/env python3

# Janyl Jumadinova
# date: 4 June 2019

DATE = "4 June 2019"
VERSION = "i"
AUTHOR = " Janyl Jumadinova"
AUTHOREMAIL = "jjumadinova@allegheny.edu"
dataDir = "SearchResults/" # all results are saved in this local directory



def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHOREMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")

        print("\n\tThe Janylka text mining tool.")
        print("\tUsage: programName <any key to launch>")
        print("\tJanylka finds everything!")
#end of help()


SUM_FILE = "sum.md"
#FILE_EXTENTION = "txt"
KEYWORDS_list = [
    "children",
    "grow meadville",
    "park", 
    "parks",
    "play",
    "youth",
    "park programs",
    "teen",
    "summer"]


class MyParser:
#class to parse each file for abstract, pmid and other details
        def __init__(self, KEYWORDS_LIST,fileList_list):
            #print "  __Welcome to parser class__"
            self.KEYWORDS_list = KEYWORDS_list # list of words, defined above
            self.fileList_list = fileList_list #list of files
            self.text_str = "" # holds the report in markdown
        #end of __init__()


        def openTextFile(self, inFile):
            #print("openTextFile(): ",inFile)
            #read a list and then restun a dic
            try: # is there a file?
                data = open(inFile).read().lower() # return a string
                return data
            except IOError:
                print("No file found... \"",inFile,"\" Exiting")
                sys.exit(1)
    #end of openTextFile()

        def goThruFiles(self): 
            """driver method in this class; opens each relevant file to send to parse"""
            fileCounter = 0 # keeps track of the relevant files to open
            # how many sum files were found?
            for i in self.fileList_list:
                if SUM_FILE in i:
                    #print(i)
                    fileCounter += 1
            counter = 1
            #print("\n  Relevant files: ")
            self.detailsText_list = [] # contains the text where the word is found
            for i in self.fileList_list: # the listing of files in the current directory
                    #print("  i: ",i)
                    if SUM_FILE in i: 
                        #print("  i: ",i)
                        currentFile = self.openTextFile(i)
                        print("   ",counter,"of", fileCounter,"|    File:",i)
                        counter += 1
                        #print("++",currentFile)
                        self.text_str = self.parser(currentFile, counter,i) #get the info from text organize it in a dictionary
            return self.text_str
        #end of goThruFiles()

        def parser(self, in_str, counter,fileName):
            """ Extracts quotes from the text files if there is a connection to a word in KEYWORDS_list"""

            # leave out the keywords section
            in_str = in_str[:in_str.find("**keywords:**")]
            " ".join(in_str.split())
            in_str = in_str.replace("\n","") #remove the white space
            #print( " in_str ;",in_str)
            #in_list = in_str.lower().replace(".","").split()
            in_list = in_str.lower().split()
            #print(" in_list :",in_list)
            text_list = []
            for word in KEYWORDS_list:
                if word in in_list:
                    wordCount = in_list.count(word)
                    print( "\t\t\t<<",word,">> found: ",wordCount, "time(s)")
                    pos0_int = in_list.index(word)
                    #print("+ :",pos0_int)
                    buffer_int = 20
                    text_list = in_list[pos0_int - buffer_int : pos0_int + buffer_int]
                    # print("  text_list :",text_list,type(text_list))
                    # put the list of text in to a string
                    self.text_str = self.text_str + "\n## File \n " + str(fileName) + "\n## Keyword \n " + str(word) + "\n## Quote \n "
                    for j in range(len(text_list)):
                        #print(text_str)
                        #print(text_list[j])
                        self.text_str = self.text_str + " " + text_list[j]
                    if wordCount > 0:
                     for wc in range(wordCount-1): # for each time the word is found
#                            print(" Current word number :" ,wc)
                            buffer_int = 20
                            pos0_int = in_list.index(word,pos0_int + 1)
                            #print("++ :",pos0_int)
                            text_list = in_list[pos0_int - buffer_int : pos0_int + buffer_int]
                            #print("++  text_list :",text_list,type(text_list))
                            # put the list of text in to a string
                            self.text_str = self.text_str + "\n## File \n " + str(fileName) + "\n## Keyword \n " + str(word) + "\n## Quote \n "
                            for j in range(len(text_list)):
                                #print(text_str)
                                #print(text_list[j])
                                self.text_str = self.text_str + " " + text_list[j] 
                    self.text_str = self.text_str + "\n___"
#                    print("  self.text_str: ",self.text_str)
            return self.text_str
        #end of parser()    

#end of class parser()


def getFileListing(corpusDir):
# method to grab all files with a particular extention
	files_list = [] # holds each file and diretory

	for root, dirs, files in os.walk(corpusDir):
		for file in files:
			#if file.endswith(FILE_EXTENTION):
                        dataFile = os.path.join(root, file)
                        files_list.append(dataFile)
	#print " getfileListing : files_list :",files_list
	return files_list

#end of getFileListing


def begin(task_str):
    """Driver function of program"""
    print(" Welcome to Janylka!")
    #print(" Task :",task_str)
    # get current directory
    cwd = os.getcwd()
    print("  Local directory    : ",cwd)
    print("  Keywords to search : ")#,KEYWORDS_list)
    printer(KEYWORDS_list)
    print("  Relevant file(s)   : ",SUM_FILE) 
    fileListing_list = getFileListing(cwd)  # get a listing of the files out there in the local dir
    #print(fileListing_list)
    j = MyParser(KEYWORDS_list, fileListing_list)
    text_str = j.goThruFiles()
    #print( "________________\nbegin() : ",text_str)
    saveFile(text_str)
#end of begin()

def saveFile(in_str):
    """Save the markdown string as a text file"""
    if len(in_str) > 0:
        try:
            tmp_dir = checkDataDir(dataDir)
            fname = "out.md"
            filename = dataDir + fname
            #f = open(dataDir + filename, "w")
            f = open(filename, "w")
            f.write(in_str)
            f.close()
            print(" + Saved md file of results in <",filename,"> ")
        except IOError:
            print("  Problem saving file... incorrect permissions?!")
	# end of saveRelationships()

def printer(inThing):
    """ prints things cleanly"""
    if "list" in str(type(inThing)):
        for i in range( len(inThing) ):
            print("   ",i,":", inThing[i])
    if "dict" in str(type(inThing)):
        counter = 0
        for i in inThing:
            print("   ",counter," |  ",i,":",inThing[i])
            counter += 1
#end of printer()


def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

    try:
        os.makedirs(dir_str)
        #print("  PROBLEM: output_dir doesn't exist")
        print("  * Creating :",dir_str)
        return 1

    except OSError:
        return 0
#end of checkDataDir()




import os, sys
if __name__ == '__main__':

        if len(sys.argv) == 2: # one parameter
                begin(sys.argv[1])#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
        else:
                help()
                sys.exit(0)

