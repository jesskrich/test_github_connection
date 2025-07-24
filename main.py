# print numbered to do list and ask if they'd like to add or delete an item. if no items exist in the list, communicate list is empty
# command 'add' triggers add function, command 'delete' triggers delete function
# add function asks what user would like to add, enter reprints the list with the added item then triggers first function again
# delete function asks for the number of the item to be deleted. once number is entered, reprint list and trigger first function again

my_list = []

def welcome_message(list):
    print_list(list)
    command = input(" type 'add' to add an item or type 'delete' to delete an item")
    if command == "add":
        command = input(" what would you like to add?")
        add_item(command,list)
        welcome_message(list)
    elif command == "delete":
        command = input(" enter the number of the item you want to delete?")
        delete_item(command, list)
    welcome_message(list)

            
def add_item(item, list):
    list.append(item)

def delete_item(item_number,list):
    del list[int(item_number) - 1]

def print_list(list):
    if not list:
        print(" You have no to-dos")
    else:
            for index, x in enumerate(list): 
                print(f"{index + 1}. {x}")

# add_item("blueberries", my_list)
# print_list(my_list) 
welcome_message(my_list)
