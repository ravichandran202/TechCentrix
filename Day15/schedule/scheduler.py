def Add_list():
    student_name = input('Enter Student Name : ')
    myfile = open(f'{student_name}_report.txt','a')
    print('Enter the details, Day : 0 to exit')
    day_count = 0
    while True:
        day = input('Day : ')
        if day == '0':
            break
        topic = input('Enter Topic : ')
        myfile.write(f'Day {day} : {topic}\n')
    myfile.close()
        
def Show_list():
    student_name = input('Enter Student Name : ')
    print('\n\n------SCHEDULER LIST------\n')
    myfile = open(f'{student_name}_report.txt','r')
    for line in myfile:
        print(line)
    print('\n--------------------------\n\n')    

def File_Operations():
    choice = int(input("Press 1 To add an items :\nPress 2 To show all items :\n"))
    if choice == 1:
        Add_list()
    elif choice == 2:
        Show_list()
    else:
        print('Please Enter Valid Input......')
    File_Operations()
File_Operations()
   