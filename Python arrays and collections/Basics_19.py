from collections import UserDict # A dictonary like object , which functions acc to users wish

class MyDict(UserDict):
    def __del__(self):
        raise RuntimeError("Cant be deleted !") # Deleting not allowed using del() function    
    def pop(self , S=None):
        raise RuntimeError("Cant be deleted !") # Deleting not allowed using pop() function
    def popitem(self , S = None):
        raise RuntimeError("Cant be deleted !") # Deleting not allowed using popitem() function

d = MyDict({1:'A' , 2:'B' , 3:'C'})
d.pop(1)