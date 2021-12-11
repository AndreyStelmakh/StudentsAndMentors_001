class Student:
    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_hw_rate()}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}"

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        else:
            return self.avg_hw_rate() == other.avg_hw_rate()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        else:
            return self.avg_hw_rate() < other.avg_hw_rate()

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def avg_hw_rate(self):
        values = []
        for values_by_course in self.grades.values():
            for value in values_by_course:
                values += [value]
        return sum(values) / (len(values) if values else 1)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        else:
            return self.avg_rate() == other.avg_rate()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        else:
            return self.avg_rate() < other.avg_rate()

    def avg_rate(self):
        values = []
        for values_by_course in self.grades.values():
            for value in values_by_course:
                values += [value]
        return sum(values) / (len(values) if values else 1)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_hw_rate_by_course(students, course):
    sum = 0
    count = 0
    for student in students:
        for hw_rate in student.grades[course]:
            sum += hw_rate
            count += 1
    result = sum / (count if count > 0 else 1)
    print(f"Средняя оценка за домашние задания по {course}:", result)


def average_lecturer_rate_by_course(lecturers, course):
    sum = 0
    count = 0
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            sum += grade
            count += 1
    result = sum / (count if count > 0 else 1)
    print(f"Средняя оценка лекторов по курсу {course}:", result)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student_2 = Student('Ewet', 'Fret', 'your_gender')
best_student_2.courses_in_progress.append('Python')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student_2, 'Python', 9.5)
cool_reviewer.rate_hw(best_student_2, 'Python', 9.5)
cool_reviewer.rate_hw(best_student_2, 'Python', 9.5)

print(best_student)
print(best_student.grades)
print(best_student.courses_in_progress)


cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Joih', 'Hsdfr')
cool_lecturer2.courses_attached += ['Python']

cool_lecturer3 = Lecturer('Sone', 'Bunny')
cool_lecturer3.courses_attached += ['Python']
cool_lecturer3.courses_attached += ['C++']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student.rate_lecturer(cool_lecturer3, 'Python', 10)
best_student.rate_lecturer(cool_lecturer3, 'Python', 9.5)

best_student_2.rate_lecturer(cool_lecturer, 'Python', 10)
best_student_2.rate_lecturer(cool_lecturer2, 'Python', 9.5)

print(cool_lecturer)

print("Сравнение студентов: ", best_student < best_student_2)
print("Сравнение лекторов", cool_lecturer < cool_lecturer3)

average_hw_rate_by_course([best_student, best_student_2], 'Python')
average_lecturer_rate_by_course([cool_lecturer, cool_lecturer2, cool_lecturer3], 'Python')
