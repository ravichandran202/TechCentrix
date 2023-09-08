shopping_list = []

def insert_list():
    input_el = input('Enter Item to Insert : ')
    shopping_list.append(input_el)
    print(f"{input_el} inserted into Shopping List")

def delete_list():
    input_el = input('Enter Item to Delete : ')
    if input_el in shopping_list:
        shopping_list.remove(input_el)
    else:
        print(f"{input_el} is not present in Shopping List")

def update_list():
    input_el = input('Enter Item to Update : ')
    if input_el in shopping_list:
        new_input = input('Enter new Item to Update : ')
        shopping_list.remove(input_el)
        shopping_list.append(new_input)
    else:
        print(f"{input_el} is not present in Shopping List")
    pass

def show_list():
    print('\n----SHOPPING LIST START----')
    for item in shopping_list:
        print(item)
    print('----SHOPPING LIST END----\n')

def shop():
    print('\n------- SHOPPING LIST --------')
    print('1. Insert')
    print('2. Delete')
    print('3. Update')
    print('4. Show List')
    choice = int(input('Enter Operation : '))
    if choice == 1:
        insert_list()
    elif choice == 2:
        delete_list()
    elif choice == 3:
        update_list()
    elif choice == 4:
        show_list()
    else:
        print('Please Enter Valid Input......')
    shop()
shop()
        