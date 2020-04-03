import os, sys, subprocess
import shutil
import binascii
import time
import getpass
import random



matches = []
matches2 = []
found = []

if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

def get_files(directory):

    filecount = 1

    print("Scanning ", directory)

    

    try:

        files = os.listdir(directory)

    except FileNotFoundError:

        print("Directory not found: " + directory)

        print("")
        mymain()  

    for i in files:

        """time.sleep(random.randint(int(0.5), int(0.5)))

        print("File " + str(filecount) + " in ", directory,": ", "\"" ,  i, "\"", end="\n")    
        """
        filecount += 1

    return files

def get_files_second_function_all_files_shown(directory):
    filecount = 1



    print("Scanning ", directory)
    

    try:

        files = os.listdir(directory)

    except FileNotFoundError:

        print("Directory not found: " + directory)

        print("")
        mymain()  

    for i in files:
        print("File " + str(filecount) + " in ", directory,": ", "\"" ,  i, "\"", end="\n")    
        
        filecount += 1

    return files



def createFile(filename, filepath):
    if sys.platform == "win32":
        file = open(filepath + "\\" + filename, "x")
    else:
        file = open(filepath + "/" + filename, "x")

def openFile(filename, filepath):
    if sys.platform == "win32":
        os.startfile(filepath + "\\" + filename)
    else:
        #changed way of opening files a little
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filepath + "\\" + filename])


def writeFile(text, filename, filepath):
    try:
        if sys.platform == "win32":
            file = open(filepath + "\\" + filename, "w")
        else:
            file = open(filepath + "/" + filename, "w")
        file.write(text)
    except:
        print("Error: 404 not found")       
    




def has_file(directory, file):

    files = get_files(directory)

    for dfile in files:

        if dfile == file:

            return True

        else:

            return False

            
def advanced_search_main():

    print("")
    file = input("Search for a file: ")
    
    print(search_user_for_file(file))
    mymain()


            
def SortDir(directory):
    files = get_files(directory)
    for eye in range(len(files)):
        try:
            filext = os.path.splitext(files[eye])
            if sys.platform == "win32":
                os.mkdir(directory + "\\" + filext[1].replace(".", ""))

              
                shutil.move(directory + "\\" + files[eye], directory + "\\" + filext[1].replace(".", "") + "\\" + files[eye])
                
            else:
                os.mkdir(directory + "/" + filext[1].replace(".", ""))

                
                shutil.move(directory + "/" + files[eye], directory + "/" + filext[1].replace(".", "") + "/" + files[eye])
                
        except:
            filext = os.path.splitext(files[eye])
            if sys.platform == "win32":
               
                
                shutil.move(directory + "\\" + files[eye], directory + "\\" + filext[1].replace(".", "") + "\\" + files[eye])
                
            else:
                

                
                shutil.move(directory + "/" + files[eye], directory + "/" + filext[1].replace(".", "") + "/" + files[eye])
                
        eye+=1


           
def get_dirs(directory):
    print("Sorry, this might take a while..")
    
    dirs = [x[0] for x in os.walk(directory)]
    print("Scaning your account.")
    print(str(len(dirs)), " directories found!")
    time.sleep(5)
    return dirs







def get_dirs_2(directory):
    print("Sorry, this might take a while..")
    
    dirs = [x[0] for x in os.walk(directory)]
    print("Scaning your account.")
    print(str(len(dirs)), " directories found!")
    print("Scanning in 5 secs")
    time.sleep(5)
    return dirs





def search_dir_for_file(directory, file):

    files = get_files(directory)

    

    for dFile in files:

        if file in dFile:

            matches.append(dFile)

        

            

        else:

            

            print("Searching for files...")

            

    if (len(matches) == 1):
        word = " File"
    else:
        word = " Files"
    if (len(matches) == 0):
        print("")
        print("no files found :(")
        print("")
        
        mymain()  
    else:
        print("")
        print(str(len(matches)) +  word + " found:")
        print("")
        for x in range(len(matches)):
            print(str(x + 1) + ". " + matches[x])
            print("")
            
            x+=1
        shouldOpen = input("open file? y/n: ")
        shouldOpen = shouldOpen.lower()
        if (shouldOpen == "y"):
            
            fileNum = input("please enter file number: ")
            try:
                openFile(matches[int(fileNum) - 1], directory + "\\")
            except OSError:
                print("Couldnt open file. Make sure you have an application associated with opening the file \"", matches[int(fileNum) - 1], "\"")
            mymain()
        else:
            print("")
            mymain()       
    

def search_user_for_file(file):
    user = "C:\\Users\\" + getpass.getuser()
    allfiles = []

    showAll = input("Show all files in directories? y/n: ")
    showAll = showAll.lower()

    if showAll == "y":
        dirs = get_dirs(user)
    else:
        dirs = get_dirs_2(user)
    





    if showAll == "y":
        for direc in dirs:
            allfiles.append(get_files_second_function_all_files_shown(direc))
    else:
        for direc in dirs:
            allfiles.append(get_files(direc))







    for fileFound in allfiles:
        matches2.append(fileFound)

    for x in range(len(matches2)):
        if file in matches2[x]:
            found.append(file)
            word = "Files "
            print (word, " found: ")
            for i in range(len(found)):
                print(str(i + 1) + ". " + found[i])
                print("Search complete!")
                mymain()
                
            
            
    


            

            





def mymain():
    try:
        print()
        cmd = input("type command(E.G. 'help'): ")
        cmd = cmd.lower() #for no case sensitivity
        if cmd == "search dir":
            matches.clear()
            direc = input("Enter directory: ")
            file = input("Search for a file: ")
            print(search_dir_for_file(direc, file))
        elif cmd == "help":
            print("commands:")
            print()
            print("search dir ( searches certain dir for a file)")
            print()
            print("search my user( your user is ", getpass.getuser(), ")")
            print()
            print("clear ( clears console writing and cache )")
            print()
            print("create file ( creates file )")
            print()
            print("open file ( opens file )")
            print()
            print("edit file ( edits file contents )")
            print()
            print("sort dir")
            print()
            print("exit")
            print()
            mymain()  
        elif cmd == "exit":
            quit()
        elif cmd == "clear":
            clear()
        elif cmd == "create file":
            FiLeNaMe = input("filename: ")
            FiLePaTh = input("filepath: ")
            createFile(FiLeNaMe, FiLePaTh)
        elif cmd == "open file":
            FILEname = input("filename: ")
            FILEpath = input("filepath: ")
            openFile(FILEname, FILEpath)
         
        elif cmd == "edit file":
            FILEnAme = input("filename: ")
            FILEpAth = input("filepath: ")
            TeXt = input("set file contents to: ")
            writeFile(TeXt,FILEnAme, FILEpAth)

        elif cmd == "search my user":
            advanced_search_main()

        elif cmd == "sort dir":
            direco = input("dir to sort: ")
            SortDir(direco)
        elif cmd == "delete dir":
            directis = input("dir to delete: ")
            os.rmdir(directis)
        else:
            print("command not found")

        mymain()
    except KeyboardInterrupt:
        print("\nExited!")
        exit(1)





  
    
    

    

    

mymain()
