from collections import UserString # A String like object , which functions acc to users wish

class MyString(UserString):
    def append(self,s): # adds the given string at the last of the string.
        self.data += s
    def remove(self,s): # Removes the desired string and replaces it with " ".
        self.data = self.data.replace(s , " ")

S = MyString('Geeks')
print(S)
print("------------------------------------------")

S.append('i')
print(S)
print("------------------------------------------")

S.remove('e')
print(S)
