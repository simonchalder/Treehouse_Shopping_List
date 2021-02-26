shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your list.
""")
    

def add_to_list(item):
    shopping_list.append(item)
    print()
    print(f'Added {item} - Number of items: {len(shopping_list)}')
    print()
    
def show_list():
    print('Current Items in List: ')
    print()
    for list_item in shopping_list:
        print(f'* {list_item}')
    

show_help()
while True:
    new_item = input("Enter item > ")
    
    if new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue # continue forces the code to return to the start of the while loop and run again
    elif new_item.upper() == 'SHOW':
        show_list()
        continue # without continue the if/elif would complete and then move on to the code after the loop
    else:
        add_to_list(new_item)

show_list()
