# from list import *

# jsonfile = input("insert json file: ")
# tasks = to_dict(jsonfile)

# while True:
#     option = input("\nEnter a number (1-6 (7 to exit)) : ")
    
#     if option == "7":
#         break
    
#     elif option == "1":
#         print(view_list(tasks))
        
#     elif option == "2":
#         mark_completed = input("enter the name task to mark completed: ")
#         new_list = completed(tasks, mark_completed)
#         print(view_list(new_list))
        
#     elif option == "3":
#         element = input("element to remove: ")
#         new_list = remove(tasks, element)
#         print(view_list(new_list))
        
#     elif option == "4":
#         element = input("enter the name of element to add: ")
#         new_list = add(tasks, element)
#         print(view_list(new_list))
        
#     elif option == "5":
#         old = input("enter the element to rename: ")
#         new = input("entre the new name: ")
#         new_list = rename(tasks, old, new)
#         print(view_list(new_list))
        
#     elif option == "6":
#         print("Coming Soon...")
    
#     else: continue


# while True:
#     jsonfile = input("Enter the list with .json: ")
#     try: tasks = to_dict(jsonfile)
#     except:
#         print("Try again.")
#         continue
#     else: break
# print(view_list(tasks))

dic = {"comer":"done", "lavar":"pending", "salir":"done"}

for key in dic:
    dic[key] = "pending"
print(dic)