import json, re

def to_dict(jsonfile):
    with open(jsonfile, 'r') as file:
        dic = json.load(file)
    return dic

def remove(dic, element):
    del dic[f"{element}"]
    return dic

def add(dic, key):
    dic[f"{key}"] = "pending"
    return dic

def rename(dic, old, new):
    dic[new] = dic.pop(old)
    return dic

def completed(dic, key):
    dic[key] = "completed"
    return dic
    
def view_list(dic):
    to_str = str(dic)
    formatted = to_str.replace("{", "\n ").replace("}", "").replace("'", "").replace(",", "\n")
    return formatted    

def save_list(dic, jsonfile):
    with open(jsonfile, 'w') as file:
        json.dump(dic, file, indent=4)


def main(): 
    print("To Do List Today")
    print("""
    0) Exit
    1) View To do list
    2) Mark Element as completed
    3) Remove an Element list
    4) Add a new Element to the list
    5) Rename Element
    6) Save list
    """)
    
    pattern = r'^[\w,\s-]+\.[Jj][Ss][Oo][Nn]$'
    while True:
        jsonfile = input("Enter the list with .json: ")
        if re.match(pattern, jsonfile):
            try: tasks = to_dict(jsonfile)
            except FileNotFoundError:
                print("Enter an existing .json file.")
                continue
            else: break
        else: print("Invalid file format. Please enter a valid .json file.")
    print(view_list(tasks))
    
    while True:
        option = input("\nSelect an option: ")
        if option == "0":
            break
        elif option == "options":
            print("""
    0) Exit
    1) View To do list
    2) Mark Element as completed
    3) Remove an Element list
    4) Add a new Element to the list
    5) Rename Element
    6) Save list
    """)
        
        elif option == "1":
            print(view_list(tasks))
            
        elif option == "2":
            mark_completed = input("enter the name task to mark completed: ")
            tasks = completed(tasks, mark_completed)
            print(view_list(tasks))
            
        elif option == "3":
            element = input("element to remove: ")
            tasks = remove(tasks, element)
            print(view_list(tasks))
            
        elif option == "4":
            element = input("enter the name of element to add: ")
            tasks = add(tasks, element)
            print(view_list(tasks))
            
        elif option == "5":
            old = input("enter the element to rename: ")
            new = input("entre the new name: ")
            tasks = rename(tasks, old, new)
            print(view_list(tasks))
        
        elif option == "6":
            save_list(tasks, jsonfile)
            print("\nList saved!")
        
        else:
            print('Options available are numbers from 1 to 6 (0 for exit and "options" to view options again).')
    
if __name__ == "__main__":
    main()