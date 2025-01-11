import json, re

# Transform json
def to_dict(jsonfile):
    with open(jsonfile, 'r') as file:
        dic = json.load(file)
    return dic

# Management
def add(dic, key):
    dic[f"{key}"] = "pending"
    return dic
def remove(dic, element):
    del dic[f"{element}"]
    return dic
def rename(dic, old, new):
    dic[new] = dic.pop(old)
    return dic

# Editing
def done(dic, key):
    dic[key] = "done"
    return dic
def pending(dic, key):
    dic[key] = "pending"
    return dic
def skipped(dic, key):
    dic[key] = "skipped"
    return dic
def failed(dic, key):
    dic[key] = "failed"
    return dic

# More Options
def all_done(dic):
    for key in dic:
        dic[key] = "done"
    return dic
def all_failed(dic):
    for key in dic:
        dic[key] = "failed"
    return dic
def all_skipped(dic):
    for key in dic:
        dic[key] = "skipped"
    return dic
def all_remove(dic):
    dic.clear()
    return dic
def reset(dic): # all as pending by default
    for key in dic:
        dic[key] = "pending"
    return dic

# Interaction
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
    1) View list                  6) Mark as Done
    2) Add new Element            7) Mark as Failed
    3) Remove an Element          8) Mark as Skipped
    4) Rename Element             9) Mark as pending
    5) More Options               0) File Name
    
        or      Exit  |  Options  |  Save
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
        if option.lower() == "exit":
            break
        elif option.lower() == "save":
            save_list(tasks, jsonfile)
            print("\nList saved!")    
        elif option.lower() == "options":
            print("""
    
    1) View list                  6) Mark as Done
    2) Add new Element            7) Mark as Failed
    3) Remove an Element          8) Mark as Skipped
    4) Rename Element             9) Mark as Pending
    5) More Options               0) File Name
    
        or      Exit  |  Options  |  Save
    """)
        
        elif option == "0":
            print(f"\n{jsonfile}")      
        elif option == "1":
            print(view_list(tasks))
        elif option == "2":
            element = input("enter the name of element to add: ")
            tasks = add(tasks, element)
            print(view_list(tasks))
        elif option == "3":
            element = input("element to remove: ")
            tasks = remove(tasks, element)
            print(view_list(tasks))
        elif option == "4":
            old = input("enter the element to rename: ")
            new = input("entre the new name: ")
            tasks = rename(tasks, old, new)
            print(view_list(tasks))
        elif option == "5":
            print("""
    Options aplied to all tasks
    1) Done
    2) Failed
    3) Skipped
    4) Removed
    5) Reset
    """)
            extra_option = input("\nSelect an option: ")
            
            if extra_option == "1":
                tasks = all_done(tasks)
                print(view_list(tasks))
            elif extra_option == "2":
                tasks = all_failed(tasks)
                print(view_list(tasks))
            elif extra_option == "3":
                tasks = all_skipped(tasks)
                print(view_list(tasks))
            elif extra_option == "4":
                tasks = all_remove(tasks)
                print(view_list(tasks))
            elif extra_option == "5":
                tasks = reset(tasks)
                print(view_list(tasks))
            else:
                print('Options available are numbers from 0 to 9 (other options are "exit", "options" and "save").')
        elif option == "6":
            mark_done = input("enter the name task to mark done: ")
            tasks = done(tasks, mark_done)
            print(view_list(tasks))
        elif option == "7":
            mark_failed = input("enter the name task to mark failed: ")
            tasks = failed(tasks, mark_failed)
            print(view_list(tasks))
        elif option == "8":
            mark_skipped = input("enter the name task to mark skipped: ")
            tasks = skipped(tasks, mark_skipped)
            print(view_list(tasks))
        elif option == "9":
            mark_pending = input("enter the name task to mark pending: ")
            tasks = pending(tasks, mark_pending)
            print(view_list(tasks))
        else: print('Options available are numbers from 1 to 9 (other options are "exit", "options" and "save").')
    
if __name__ == "__main__":
    main()