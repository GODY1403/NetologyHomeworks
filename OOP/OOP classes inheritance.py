class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def make_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        for course, marks in self.grades.items():
            if len(marks) == 0:
                print(f"Курс {course}: Нет оценок")
            else:
                average = sum(marks) / len(marks)
                return average

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средний баллл за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе: {", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов"}\n'
                f'Завершённые курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нет завершённых курсов"}')

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    @staticmethod
    def average_grade_all_students(students, course):
        all_grades = []
        for student in students:
            if course in student.grades:
                all_grades.extend(student.grades[course])
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade():.1f}"
        )

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    @staticmethod
    def average_grade_all_lecturers(lecturers, course):
        all_grades = []
        for lecturer in lecturers:
            if course in lecturer.grades:
                all_grades.extend(lecturer.grades[course])
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# Лекторы
Egor_M = Lecturer('Egor', 'Myasnikov')
Egor_M.courses_attached += ['Python']
Egor_M.courses_attached += ['Java']

Kiril_T = Lecturer("Kiril", "Tapkov")
Kiril_T.courses_attached += ['Java']

Ibragim_R = Lecturer('Ibragim', 'Rimskiy')
Ibragim_R.courses_attached += ['Python']

# Проверяющие
Anthon_V = Reviewer('Anthon', 'Volkov')
Anthon_V.courses_attached += ['Python']

Efrim_L = Reviewer('Efrim', 'Lemonov')
Efrim_L.courses_attached += ['Java']

# Студенты
Vladislav_P = Student('Vladislav', 'Popov', 'Male')
Vladislav_P.courses_in_progress += ['Python']
Vladislav_P.courses_in_progress += ['Java']
Vladislav_P.finished_courses += ['Отладка кода']

Evgeniy_T = Student('Evgeniy', 'Tortov', 'Male')
Evgeniy_T.courses_in_progress += ['Java']

Genadiy_G = Student('Genadiy', 'Galkin', 'Male')
Genadiy_G.courses_in_progress += ['Python']

# Проверки работоспособности кода
# Оценка студентов проверяющими
Anthon_V.rate_hw(Vladislav_P, 'Python', 10)
Anthon_V.rate_hw(Vladislav_P, 'Python', 1)
Anthon_V.rate_hw(Vladislav_P, 'Python', 10)

Anthon_V.rate_hw(Genadiy_G, 'Python', 10)
Anthon_V.rate_hw(Genadiy_G, 'Python', 1)
Anthon_V.rate_hw(Genadiy_G, 'Python', 10)

Efrim_L.rate_hw(Vladislav_P, 'Java', 3)
Efrim_L.rate_hw(Vladislav_P, 'Java', 4)
Efrim_L.rate_hw(Vladislav_P, 'Java', 7)

Efrim_L.rate_hw(Evgeniy_T, 'Java', 6)
Efrim_L.rate_hw(Evgeniy_T, 'Java', 10)
Efrim_L.rate_hw(Evgeniy_T, 'Java', 8)

# Оценка лекторов студентами
Vladislav_P.make_grade(Egor_M, 'Python', 10)
Vladislav_P.make_grade(Egor_M, 'Python', 10)
Vladislav_P.make_grade(Egor_M, 'Python', 10)

Vladislav_P.make_grade(Egor_M, 'Java', 3)
Vladislav_P.make_grade(Egor_M, 'Java', 1)
Vladislav_P.make_grade(Egor_M, 'Java', 9)

Evgeniy_T.make_grade(Egor_M, 'Java', 9)
Evgeniy_T.make_grade(Egor_M, 'Java', 5)
Evgeniy_T.make_grade(Egor_M, 'Java', 3)

Vladislav_P.make_grade(Ibragim_R, 'Python', 10)
Vladislav_P.make_grade(Ibragim_R, 'Python', 6)
Vladislav_P.make_grade(Ibragim_R, 'Python', 7)

Evgeniy_T.make_grade(Kiril_T, 'Java', 4)
Evgeniy_T.make_grade(Kiril_T, 'Java', 3)
Evgeniy_T.make_grade(Kiril_T, 'Java', 8)

print(Vladislav_P)
print(f"")
print(Anthon_V)
print(f"")
print(Egor_M)
print(f'')
print(Genadiy_G)
print(f'')
print(Ibragim_R)
print(f'')
print(Kiril_T)
print(f'')

# Сравнение студентов
print(Vladislav_P == Genadiy_G)
print(Vladislav_P != Genadiy_G)
print(Vladislav_P <= Genadiy_G)
print(Vladislav_P >= Genadiy_G)

print('')
# Сравнение лекторов
print(Ibragim_R == Egor_M)
print(Ibragim_R != Kiril_T)
print(Kiril_T <= Egor_M)
print(Ibragim_R >= Egor_M)

print("")
# Подсчет средней оценки за домашние задания по всем студентам в рамках курса 'Python'
students = [Vladislav_P, Genadiy_G, Evgeniy_T]
print(f"Средняя оценка за домашние задания по курсу: {Student.average_grade_all_students(students, 'Python')}")

# Подсчет средней оценки за лекции всех лекторов в рамках курса 'Java'
lecturers = [Egor_M, Kiril_T, Ibragim_R]
print(f"Средняя оценка за лекции по курсу: {Lecturer.average_grade_all_lecturers(lecturers, 'Java')}")
