class User:
    def __init__(self, name):
        self.name = name

    def get_dashboard(self):
        return f"{self.name} uchun bosh sahifa yuklanmoqda..."


class Student(User):
    def __init__(self, name, enrolled_courses):
        super().__init__(name)
        self.enrolled_courses = enrolled_courses

    def get_dashboard(self):
        course_list = ", ".join(self.enrolled_courses)
        return (
            f"Talaba: {self.name}\n"
            f"O'qiyotgan kurslar: {course_list}"
        )


class Instructor(User):
    def __init__(self, name, teaching_courses, students_count):
        super().__init__(name)
        self.teaching_courses = teaching_courses
        self.students_count = students_count

    def get_dashboard(self):
        course_list = ", ".join(self.teaching_courses)
        return (
            f"O'qituvchi: {self.name}\n"
            f"O'qitayotgan kurslar: {course_list}\n"
            f"Umumiy talabalar soni: {self.students_count}"
        )


users = [
    Student("Ali", ["Python", "Django", "Git"]),
    Instructor("Vali", ["Python", "Machine Learning"], 85),
]

for user in users:
    print(user.get_dashboard())
    print()
