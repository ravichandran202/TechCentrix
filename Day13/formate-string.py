name = 'Ravi'
marks = 100
program = 'Python Program'


print('Welcome to python program, '+name)

print(name,'Scored',marks,'Marks in',program)

print(f"{name} Scored {marks} Marks in {program}")

print("%s Scored %d Marks in %s" %(name,marks,program))

print("{} scored {} Marks in {}".format(name,marks,program))

print("{1} scored {0} Marks in {2}".format(marks,name,program))
