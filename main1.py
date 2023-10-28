# # Task 1: Create a program which takes the name of a user and prints a message to him:

# Username = [
#     {
#         "name": "Name",
#         "type": "list",
#         "choices": ["Sauleh","Hira","Other"],
#         "message": "What is your name?"
#     }
# ]

# result = prompt(Username)
# username = result["Name"]
# print(f"Hi there {username}!")

# print(f"Hello world"); 

# # I am not getting option, only python 3.11.6 and 3.11.5

# # It is not downloading numpy, but everything else it is dowloading.

# name = "Mohammad Qasim"
# print(name)
# print(type(name))
# print(id(name))sd
# print(dir(name))

# names: str = 1200
# print(names)

# a = int(input("Enter a number: "))
# print(a)

# pythonList: list[str] = ["Hey","Bay","Hay"]

# pythonList.extend("HeyLo")

# print(pythonList)

bag: list = []

def Addinbag():
    while True:    
        a = input("What to add in the bag? Say 'Quit' to stop adding items")
        if a:
            bag.append(a)
        elif a == "Quit":
            print("Here is your bag:")
            print(bag)
            break
        else:
            break
        
Addinbag()