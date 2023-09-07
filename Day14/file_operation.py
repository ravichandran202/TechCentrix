myfile = open('myfile.txt','w')
myfile.write('New line added into file')
myfile.close()

myfile = open('myfile.txt','a')
myfile.write('\nappend line added into file')
myfile.close()

myfile = open('myfile.txt','r')
print(myfile.read())
myfile.close()

myfile = open('myfile.txt','r')
print(myfile.readline())
myfile.close()

myfile = open('myfile.txt','r')
print(myfile.readlines())
myfile.close()
