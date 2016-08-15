"""

Miguel Verroya
"""
name = input("Please Enter Name")

while name == "":
    name = input("Please Enter Name")

for i in range(0, len(name), 2):
    print(name[i], end='')

