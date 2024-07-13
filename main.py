list=[]
with open('todo.txt', 'r') as file:
  for line in file:
    list.append(line.strip())
def display():
    a=input("Would you like to:\n(1)Add something to your list\n(2)View your list\n(3)Delete an item from you list\n(4)clear list\n")
    if a=="1":
        add()
    elif a=="2":
        view()
    elif a=="3":
        delete()
    elif a=="4":
        clear()
def add():
    a=input("Enter in what you would like to add\n")
    list.append(a)
    print("Added item")
    x=0
    with open('todo.txt', 'w') as file:
       while x<len(list):
        file.write(list[x]+"\n")
        x+=1
    display()
def view():
    x=0
    print(f"You have {len(list)} things left to do")
    while x<len(list):
        print(f"{x+1}:{list[x]}")
        x+=1
    display()
def delete():
    a=int(input("Which item would you like to delete?\n"))
    list.pop(a-1)
    print("Item removed.")
    x=0
    with open('todo.txt', 'w') as file:
           while x<len(list):
            file.write(list[x]+"\n")
            x+=1
    display()
def clear():
    list.clear()
    print("List cleared")
    with open('todo.txt', 'w') as file:
          file.write("")
    display()
display()
