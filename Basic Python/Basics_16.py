from collections import namedtuple

S = namedtuple('student' , ['name' , 'age' , 'DOB'])
SD = S('nandini' , '19' , '2451997')

l = ['manjeet' , '19' , '151997']
d = {'name' : "ram" , 'age' : "19" , "dob" : "1391997"}

print(SD)
print(SD._make(l))
print(SD._asdict())

