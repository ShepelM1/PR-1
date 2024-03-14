class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name}, {self.age} years")


class Employee(Person):

    def __init__(self, name, age, position):

        super().__init__(name, age)
        self.position = position

    def work(self):
        print(f"{self.name}, {self.age} - {self.position}")


class Student(Person):

    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name}, {self.age} - {self.student_id}")


class University:
    def __init__(self):
        self.employees = []
        self.students = []

    def add_student_to_list(self, student):
        self.students.append(student)

    def add_employee_to_list(self, employee):
        self.employees.append(employee)

    def remove_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def remove_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return True
        return False

    def find_person_by_name(self, name):
        for person in self.employees + self.students:
            if person.name == name:
                return person
        return None

    def find_person_by_id(self, student_id):
        for person in self.students:
            if isinstance(person, Student) and person.student_id == student_id:
                return person
        return None

    def show_info(self):
        print("Employees:")
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}")
        print("Students:")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Student ID: {student.student_id}")


university = University()

employee = Employee("John", 30, "Professor")
student = Student(1, "Kolya", 18)
university.add_employee_to_list(employee)
university.add_student_to_list(student)

university.show_info()

university.remove_employee_by_name("John")
university.remove_student_by_id(1)

found_person = university.find_person_by_name("Kolya")
if found_person:
    print(f"Found person: {found_person.name}")
else:
    print("Person not found")

found_student = university.find_person_by_id(1)
if found_student:
    print(f"Found student: {found_student.name}")
else:
    print("Student not found")


