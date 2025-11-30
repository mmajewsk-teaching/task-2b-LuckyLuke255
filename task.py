import random


def get_courses():
    courses = []
    course_names = ["Math", "Physics", "Chemistry", "History", "English", "Biology"]

    for name in course_names:
        courses.append(name)

    return courses


def generate_students(courses, number_of_students):
    schools = []
    schools.append("School A")
    schools.append("School B")
    lines = []
    index = 0

    while index < number_of_students:
        name = "Student_" + str(index + 1)
        if index % 2 == 0:
            school = schools[0]
        else:
            school = schools[1]

        grades_text_list = []
        course_index = 0
        while course_index < len(courses):
            grade_value = random.randint(1, 6)
            grades_text_list.append(str(grade_value))
            course_index += 1

        grades_text = ",".join(grades_text_list)
        line = name + ";" + school + ";" + grades_text
        lines.append(line)

        index += 1

    return lines


def save_students_to_file(filename, lines):
    file_object = open(filename, "w", encoding="utf-8")
    for line in lines:
        file_object.write(line)
        file_object.write("\n")
    file_object.close()


def load_students_from_file(filename):
    lines = []
    file_object = open(filename, "r", encoding="utf-8")
    for line in file_object:
        text_line = line.strip()
        if text_line != "":
            lines.append(text_line)
    file_object.close()
    return lines


def parse_students(lines, number_of_courses):
    students = []
    for line in lines:
        parts = line.split(";")
        name = parts[0]
        school = parts[1]
        grades_text = parts[2]
        grade_strings = grades_text.split(",")
        grades = list(map(int, grade_strings))
        if len(grades) > number_of_courses:
            grades = grades[:number_of_courses]
        student = {
            "name": name,
            "school": school,
            "grades": grades,
        }
        students.append(student)
    return students


def calculate_list_average(numbers):
    if not numbers:
        return 0.0
    total = 0
    count = 0
    for value in numbers:
        total = total + value
        count = count + 1
    result = total / count
    return result


def calculate_course_averages(students, courses):
    course_averages = {}
    course_index = 0
    while course_index < len(courses):
        course_name = courses[course_index]
        total = 0
        count = 0
        for student in students:
            grades = student["grades"]
            if course_index < len(grades):
                total = total + grades[course_index]
                count = count + 1
        if count > 0:
            average_value = total / count
        else:
            average_value = 0.0
        course_averages[course_name] = average_value
        course_index = course_index + 1
    return course_averages


def calculate_student_averages(students):
    student_averages = {}
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average_value = calculate_list_average(grades)
        student_averages[name] = average_value
    return student_averages


def calculate_school_averages(students):
    school_students = {}
    for student in students:
        school = student["school"]
        if school not in school_students:
            school_students[school] = []
        school_students[school].append(student)

    school_averages = {}
    for school_name in school_students:
        all_grades = []
        students_in_school = school_students[school_name]
        for student in students_in_school:
            grades = student["grades"]
            for grade_value in grades:
                all_grades.append(grade_value)
        average_value = calculate_list_average(all_grades)
        school_averages[school_name] = average_value

    return school_averages


def write_report(filename,courses,course_averages,student_averages,school_averages):
    file_object = open(filename, "w", encoding="utf-8")

    file_object.write("Average grade per course:\n")
    for course_name in courses:
        if course_name in course_averages:
            average_value = course_averages[course_name]
            line = course_name + ": " + f"{average_value:.2f}"
            file_object.write(line)
            file_object.write("\n")

    file_object.write("\nAverage grade per student:\n")
    for student_name in student_averages:
        average_value = student_averages[student_name]
        line = student_name + ": " + f"{average_value:.2f}"
        file_object.write(line)
        file_object.write("\n")

    file_object.write("\nAverage grade per school:\n")
    for school_name in school_averages:
        average_value = school_averages[school_name]
        line = school_name + ": " + f"{average_value:.2f}"
        file_object.write(line)
        file_object.write("\n")

    file_object.close()


def main():
    courses = get_courses()
    number_of_students = 20
    student_lines = generate_students(courses, number_of_students)
    save_students_to_file("students.txt", student_lines)
    loaded_lines = load_students_from_file("students.txt")
    students = parse_students(loaded_lines, len(courses))
    course_averages = calculate_course_averages(students, courses)
    student_averages = calculate_student_averages(students)
    school_averages = calculate_school_averages(students)
    write_report(
        "report.txt",
        courses,
        course_averages,
        student_averages,
        school_averages,
    )


if __name__ == "__main__":
    main()
