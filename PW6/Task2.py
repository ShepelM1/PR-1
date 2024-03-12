class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name}, {self.age} years")


class Employee(Person):

    def __init__(self, name, age, position):

        self.position = position

    def work(self):
        print(f"{self.name}, {self.age} - {self.position}")


class Student(Person):

    def __init__(self, student_id, name, age):

        self.student_id = student_id

    def study(self):
        print(f"{self.name}, {self.age} - {self.student_id}")


class University:
    def __init__(self, employee, student):
        self.employee = []
        self.student = []

    def add_student_to_list(self, student_id, name, age):
        return self.student.append([student_id, name, age])

    def add_employee_to_list(self, name, age, position):
        return self.employee.append([name, age, position])


student = Student(1, "Kolya", 18)
University.add_student_to_list(student)

