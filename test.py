from list import *
    
jsonfile = input("insert json file: ")
tasks = to_dict(jsonfile)

while True:
    option = input("\nEnter a number (1-7): ")
    
    if option == "exit":
        break
    
    elif option == "1":
        print(view_list(tasks))
        
    elif option == "2":
        value_to_remove = input("enter the name taks to remove: ")
        dic = completed(tasks, value_to_remove)
        print(view_list(dic))
        
    else: continue