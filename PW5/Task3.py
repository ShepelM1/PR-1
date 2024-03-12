class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name
        return self.name


class Student(Human):
    def __init__(self, vnz, list_grades):
        self.vnz = vnz
        self.list_grades = list_grades

    def add_grade_to_list(self, grade):
        return self.list_grades.append(grade)

    def average_grade(self):
        return sum(self.list_grades)/len(self.list_grades)


human = Human("Kolya", 18)

print(f"Ім'я студента - {human.name}")

human.change_name("Pasha")

student = Student("IPZ", [3, 5, 4])
student.add_grade_to_list(int(input("Введіть оцінку: ")))

print(f"Ім'я студента - {human.name} \n"
      f"Оцінки студента - {student.list_grades} \n"
      f"Середній бал - {student.average_grade()}")
