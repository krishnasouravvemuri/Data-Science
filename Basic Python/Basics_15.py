from collections import namedtuple

S = namedtuple('student' , ['name' , 'age' , 'DOB'])
SD = S('nandini' , '19' , '2451997')
print(SD[0]) # Accessing the tuple by index
print(SD.age) # Accessing the tuple by the name
