from typing import TypedDict

#  typedic is just show the type of variable which type of that 

class User(TypedDict):
    name: str
    age: int

new_user: User = {'name': 'Farman Ali', 'age': 25}
print(new_user) 