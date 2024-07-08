f2 = open("file1.txt",'w')
f2.write("Line1 of file1 \n")
f2.close()


f1 = open("./Python DA/File Handling/file1.txt",'r+')
# f1.write("Written using r+ mode \n")
print(f1.read())
# print(f1.readlines())
f1.close()

f3 = open("./Python DA/File Handling/file1.txt",'a')
f3.write("Line3 appended using append mode \n")
f3.close()

'''
f4 = open("./Python DA/File Handling/file1.txt",'a+')
f4.write("NOthing \n")
print(f4.read())
f4.close
'''

f5 = open("./Python DA/File Handling/file1.txt",'r')
print(f5.read(10))
f5.close()

# When you use write mode for existing file it overwrites the data.
