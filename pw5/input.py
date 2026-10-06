import curses
import math
from domains import Student, Course

def get_input(stdscr, prompt, y, x):
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    curses.echo()
    user_input = stdscr.getstr(y, x + len(prompt)).decode('utf-8')
    curses.noecho()
    return user_input

def add_students(stdscr, students_list):
    stdscr.clear()
    try:
        num = int(get_input(stdscr, "Enter number of students: ", 0, 0))
        for i in range(num):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Student {i+1}/{num}")
            sid = get_input(stdscr, "ID: ", 1, 0)
            name = get_input(stdscr, "Name: ", 2, 0)
            dob = get_input(stdscr, "DOB (DD/MM/YYYY): ", 3, 0)
            students_list.append(Student(sid, name, dob))
        stdscr.addstr(5, 0, "Students added successfully! Press any key.")
        
        with open("students.txt", "w") as f:
            for s in students_list:
                f.write(f"{s.student_id},{s.name},{s.dob}\n")
    except ValueError:
        stdscr.addstr(5, 0, "Invalid input! Press any key.")
    stdscr.getch()

def add_courses(stdscr, courses_list):
    stdscr.clear()
    try:
        num = int(get_input(stdscr, "Enter number of courses: ", 0, 0))
        for i in range(num):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Course {i+1}/{num}")
            cid = get_input(stdscr, "ID: ", 1, 0)
            name = get_input(stdscr, "Name: ", 2, 0)
            credits = int(get_input(stdscr, "Credits: ", 3, 0))
            courses_list.append(Course(cid, name, credits))
        stdscr.addstr(5, 0, "Courses added successfully! Press any key.")
        
        with open("courses.txt", "w") as f:
            for c in courses_list:
                f.write(f"{c.course_id},{c.name},{c.credits}\n")
    except ValueError:
        stdscr.addstr(5, 0, "Invalid input! Press any key.")
    stdscr.getch()

def input_marks(stdscr, students_list, courses_list):
    stdscr.clear()
    if not students_list or not courses_list:
        stdscr.addstr(0, 0, "Please add students and courses first! Press any key.")
        stdscr.getch()
        return
        
    cid = get_input(stdscr, "Enter course ID to input marks: ", 0, 0)
    course = next((c for c in courses_list if c.course_id == cid), None)
    
    if not course:
        stdscr.addstr(2, 0, "Course not found! Press any key.")
        stdscr.getch()
        return
        
    stdscr.addstr(2, 0, f"Inputting marks for course {course.name}")
    row = 3
    for student in students_list:
        try:
            raw_score = float(get_input(stdscr, f"Mark for {student.name}: ", row, 0))
            # Use math module to round-down to 1-digit decimal
            rounded_score = math.floor(raw_score * 10) / 10.0
            student.marks[cid] = rounded_score
            student.calculate_gpa(courses_list)
        except ValueError:
            stdscr.addstr(row+1, 0, "Invalid mark! Skipping.")
            row += 1
        row += 1
        
    with open("marks.txt", "w") as f:
        for s in students_list:
            for c_id, mark in s.marks.items():
                f.write(f"{s.student_id},{c_id},{mark}\n")
                
    stdscr.addstr(row + 1, 0, "Marks added successfully! Press any key.")
    stdscr.getch()