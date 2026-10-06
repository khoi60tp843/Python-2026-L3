import curses
import os
import zipfile
from input import add_students, add_courses, input_marks
from output import show_students, show_courses, show_marks
from domains import Student, Course

def load_data(students, courses):
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as z:
            z.extractall()
            
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        courses.append(Course(parts[0], parts[1], int(parts[2])))
                        
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        students.append(Student(parts[0], parts[1], parts[2]))
                        
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        sid, cid, mark = parts[0], parts[1], float(parts[2])
                        for s in students:
                            if s.student_id == sid:
                                s.marks[cid] = mark
                                s.calculate_gpa(courses)
                                break

def compress_data():
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as z:
        if os.path.exists("students.txt"):
            z.write("students.txt")
        if os.path.exists("courses.txt"):
            z.write("courses.txt")
        if os.path.exists("marks.txt"):
            z.write("marks.txt")

def main(stdscr):
    # Data storage
    students = []
    courses = []

    # Load data from students.dat
    load_data(students, courses)

    curses.curs_set(0) # Hide cursor
    stdscr.keypad(True)
    
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Mark Management System", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Add Students")
        stdscr.addstr(3, 0, "2. Add Courses")
        stdscr.addstr(4, 0, "3. Input Marks")
        stdscr.addstr(5, 0, "4. Show Students (sorted by GPA)")
        stdscr.addstr(6, 0, "5. Show Courses")
        stdscr.addstr(7, 0, "6. Show Marks")
        stdscr.addstr(8, 0, "0. Exit")
        stdscr.addstr(10, 0, "Enter your choice: ")
        
        stdscr.refresh()
        curses.echo()
        choice = stdscr.getstr(10, 19).decode('utf-8')
        curses.noecho()
        
        if choice == '1':
            add_students(stdscr, students)
        elif choice == '2':
            add_courses(stdscr, courses)
        elif choice == '3':
            input_marks(stdscr, students, courses)
        elif choice == '4':
            show_students(stdscr, students)
        elif choice == '5':
            show_courses(stdscr, courses)
        elif choice == '6':
            show_marks(stdscr, students, courses)
        elif choice == '0':
            compress_data()
            break
        else:
            stdscr.addstr(12, 0, "Invalid choice! Press any key to continue.")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
