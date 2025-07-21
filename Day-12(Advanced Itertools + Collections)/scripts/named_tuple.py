from collections import namedtuple

Student = namedtuple("Student,[name, age, score]")
s1 = Student("Michael", 20, 88)
s2 = Student("Bob", 19, 90)
s3 = Student("Tracy", 21, 85)

print(s1.name, s1.age, s1.score)
print(s2.name, s2.age, s2.score)
print(s3.name, s3.age, s3.score)
print(s1)
print(s2)
print(s3)
print(s1._fields)
print(s1._asdict())
