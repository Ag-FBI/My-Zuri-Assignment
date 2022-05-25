class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass



first_student = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(first_student.name)
print(first_student.age)
print(first_student.tracks)
print(first_student.score)

new_student = Student( name= input("change_name here : "), age= input("change_age here : "), tracks= input("add_track here :"), score = float(30.25))  
print(new_student.name)
print(new_student.age)
print(new_student.tracks)
print(new_student.score) 
 


# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
