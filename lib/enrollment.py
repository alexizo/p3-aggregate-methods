class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, enrollment):
        self._enrollments.append(enrollment)

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return None
        
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses
        return average_grade


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrollments = []


class Enrollment:
    all_enrollments = []

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        student.enroll(self)
        course.enrollments.append(self)
        Enrollment.all_enrollments.append(self)

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all_enrollments:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


student1 = Student('John Doe')
student2 = Student('Jane Smith')

course1 = Course('Mathematics')
course2 = Course('Science')

import datetime
enrollment1 = Enrollment(student1, course1, datetime.datetime(2023, 9, 22))
enrollment2 = Enrollment(student1, course2, datetime.datetime(2023, 9, 22))
enrollment3 = Enrollment(student2, course1, datetime.datetime(2023, 9, 23))

student1._grades[enrollment1] = 85
student1._grades[enrollment2] = 90

print(f"{student1.name} is enrolled in {student1.course_count()} courses.")

average_grade = student1.aggregate_average_grade()
if average_grade is not None:
    print(f"Average grade for {student1.name}: {average_grade:.2f}")
else:
    print(f"No grades available for {student1.name}")

enrollment_counts = Enrollment.aggregate_enrollments_per_day()
print("Enrollments per day:")
for date, count in enrollment_counts.items():
    print(f"{date}: {count} enrollments")
