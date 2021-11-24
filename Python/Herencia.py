class Person:
    def __init__(self, first_n, last_n):
        self.first_n = first_n
        self.last_n = last_n

    def say_hello_user(self, username):
        return("Hi, "+ username)

    def say_hello_person(self, first_n, last_n):
        return ("Hello, "+first_n+ " "+last_n)



object_person = Person("Cesar", "Gonzalez")
print(object_person.say_hello_user("Charlie"))
print(object_person.say_hello_person(object_person.first_n, object_person.last_n))



class Student(Person):

    def __init__(self, first_n, last_n, aka_name):
        super().__init__(first_n, last_n)
        self.aka_name = aka_name

    def nick_name(self, aka_name):
        return ("AKA: "+ aka_name)

    def student_id(self, student_id):
        return ("Matricula: " + str(student_id))


object_student = Student ("Omar ", "Muguia", "ZIZA")
print(object_student.say_hello_person(object_student.first_n, object_student.last_n))
print(object_student.nick_name(object_student.aka_name))
print(object_student.student_id(1303840))


class Teacher(Person):

    def __init__(self, first_n, last_n):
        super().__init__(first_n, last_n)


    def id_teacher(self, teacher_id):
        return ("Matricula: "+ str(teacher_id))

    def greet_student(self, student_name):
        return("Hi "+ student_name+ "Im your teacher "+ self.first_n +" "+self.last_n)



object_teacher = Teacher ("Luis", "Guerra")
print(object_teacher.say_hello_person(object_teacher.first_n, object_teacher.last_n))
print(object_teacher.greet_student(object_student.first_n))
print(object_teacher.id_teacher(154367))


class Basic_student(Person):
    def __init__(self, first_n, last_n, grade, age, school_name):
        super().__init__(first_n, last_n)
        self.grade = grade
        self.age = age
        self.school_name = school_name

    def basic_student_grade(self, grade):
        return("Grade: "+grade)

    def basic_student_age(self, age):
        return ("The student name is: " + object_basic_student.first_n + " "+ object_basic_student.last_n +"His age is: "+ age)

    def basic_student_school_name(self, school_name):
        return("School name: "+school_name)


object_basic_student = Basic_student ("Axel", "Gonzalez\n", "8vo", "12 years", "Univa")

print(object_basic_student.basic_student_grade(object_basic_student.grade))
print(object_basic_student.basic_student_age(object_basic_student.age))
print(object_basic_student.basic_student_school_name(object_basic_student.school_name))




