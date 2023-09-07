def add(value1,value2):
    result = value1 + value2
    return result

def sub(value1,value2):
    result = value1 - value2
    return result

def mul(value1,value2):
    result = value1 * value2
    return result

def div(value1,value2):
    if value2 == 0:
        return 'Cannot divide by 0'
    result = value1 / value2
    return result

# def calculator():
#     while True:
#         print('\n\n----------BASIC CALCULATOR----------')
#         print('1.Addition       2.Subtraction \n3.Multiplication 4.Division \n5.Exit')
#         print('------------------------------------')
#         choice = int(input('Enter Your choice :'))
#         if choice == 5:
#             return
        
#         value1 = int(input('Enter Number 1 :'))
#         value2 = int(input('Enter Number 2 :'))
#         result = 0
        
#         if choice == 1:
#             result = add(value1,value2)
#         elif choice == 2:
#             result = sub(value1,value2)
#         elif choice == 3:
#             result = mul(value1,value2)
#         elif choice == 4:
#             result = div(value1,value2)
#         else:
#             result = 'Please Enter valid choice'
#         print(f'Result : {result}')

# calculator()