import json

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
    dic[f"{new}"] = dic.pop(f"{old}")
    return dic

def completed(dic, key):
    dic[f"{key}"] = "completed"
    return dic
    
def view_list(dic):
    to_str = str(dic)
    formated = to_str.replace("{", "\n ").replace("}", "").replace("'", "").replace(",", "\n")
    return formated    


def main(): 
    print("To Do List Today")
    print("""
    1) View To do list
    2) Mark Element as completed
    3) Remove an Element list
    4) Add a new Element to the list
    5) Rename Element
    6) Save list (coming soon)
    7) Exit
        """)
    jsonfile = input("Enter the list with .json: ")
    jsonfile = to_dict(jsonfile)
    print(view_list(jsonfile))
    
if __name__ == "__main__":
    main()