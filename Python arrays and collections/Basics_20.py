from collections import UserList # A list like object , which functions acc to users wish
class MyList(UserList):
    def remove(self , S=None):
        raise RuntimeError("Cant be deleted !") # Deleting not allowed using del() function    
    def pop(self , S=None):
        raise RuntimeError("Cant be deleted !") # Deleting not allowed using pop() function

l = MyList([1,2,3,4,5,6,7])
l.pop(1)