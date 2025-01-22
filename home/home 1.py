'''' Создать класс Person с атрибутами full_name, age, is_married

2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке

3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.

4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам

5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience. 

6. Добавить в класс Teacher атрибут уровня класса base_salary.

7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.

8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.

10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам. '''''



class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "Married" if self.is_married else "Not Married"
        print(f"Name: {self.full_name}, Age: {self.age}, Marital Status: {marital_status}")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = Teacher.base_salary * 0.05 * bonus_years
        else:
            bonus = 0
        return Teacher.base_salary + bonus

def create_students():
    student1 = Student("Alice Brown", 16, False, {"Math": 85, "English": 90, "History": 78})
    student2 = Student("Bob Smith", 17, False, {"Math": 92, "English": 88, "History": 84})
    student3 = Student("Charlie Green", 16, False, {"Math": 75, "English": 80, "History": 89})
    return [student1, student2, student3]

# Creating a teacher object
teacher = Teacher("John Doe", 45, True, 10)
teacher.introduce_myself()
print(f"Salary: {teacher.calculate_salary()}\n")

# Creating students and displaying their information
students = create_students()
for student in students:
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"  {subject}: {mark}")
    print(f"Average Mark: {student.calculate_average_mark()}\n")
