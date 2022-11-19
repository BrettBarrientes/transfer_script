import os
#Script's purpose is to rename and move files from List 1 directory to List 2 directory.
#Instead of moving files one at a time, this script will move multiple files to different directories all at once in a loop.


List1 = ['C:/Users/[Name]/Documents/New-Path-Test/test1.txt', 'C:/Users/[Name]/Documents/New-Path-Test/test2.txt',
            "C:/Users/[Name]/Documents/New-Path-Test/test3.txt"] #List of the Old directories

List2 = ['C:/Users/[Name]/1222/Remaining useful life.txt','C:/Users/[Name]/1223/Remaining useful life.txt',
            'C:/Users/[Name]/1224/Remaining useful life.txt'] #List of the New Directories


for i in range(len(List1)): # range of the array will be 2 since the index is counting from 0-2
    if i == 2:
        print(os.rename(List1[0], List2[0])) #i = index 0 C:/Users/Brett/Documents/New-Path-Test/test1.txt --> C:/Users/Brett/1222/Remaining useful life.txt
        print(os.rename(List1[1], List2[1])) #i = index 1 C:/Users/Brett/Documents/New-Path-Test/test2.txt --> C:/Users/Brett/1223/Remaining useful life.txt
        print(os.rename(List1[2], List2[2])) #i = index 2 C:/Users/Brett/Documents/New-Path-Test/test3.txt --> C:/Users/Brett/1224/Remaining useful life.txt
