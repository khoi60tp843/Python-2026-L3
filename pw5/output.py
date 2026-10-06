import curses
import numpy as np
from input import get_input

def show_students(stdscr, students_list):
    stdscr.clear()
    
    # Sort student list by GPA descending using numpy array
    if students_list:
        gpas = np.array([s.gpa for s in students_list])
        sorted_indices = np.argsort(gpas)[::-1]
        sorted_students = [students_list[i] for i in sorted_indices]
    else:
        sorted_students = []
        
    stdscr.addstr(0, 0, "List of Students (Sorted by GPA):", curses.A_BOLD)
    stdscr.addstr(1, 0, f"{'ID':<10} | {'Name':<20} | {'DOB':<15} | {'GPA':<5}")
    stdscr.addstr(2, 0, "-" * 55)
    
    for i, s in enumerate(sorted_students):
        stdscr.addstr(3 + i, 0, f"{s.student_id:<10} | {s.name:<20} | {s.dob:<15} | {s.gpa:<5}")
        
    stdscr.addstr(5 + len(sorted_students), 0, "Press any key to return.")
    stdscr.getch()

def show_courses(stdscr, courses_list):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of Courses:", curses.A_BOLD)
    stdscr.addstr(1, 0, f"{'ID':<10} | {'Name':<20} | {'Credits':<10}")
    stdscr.addstr(2, 0, "-" * 45)
    
    for i, c in enumerate(courses_list):
        stdscr.addstr(3 + i, 0, f"{c.course_id:<10} | {c.name:<20} | {c.credits:<10}")
        
    stdscr.addstr(5 + len(courses_list), 0, "Press any key to return.")
    stdscr.getch()

def show_marks(stdscr, students_list, courses_list):
    stdscr.clear()
    cid = get_input(stdscr, "Enter course ID to view marks: ", 0, 0)
    course = next((c for c in courses_list if c.course_id == cid), None)
    
    if not course:
        stdscr.addstr(2, 0, "Course not found! Press any key.")
        stdscr.getch()
        return
        
    stdscr.addstr(2, 0, f"Marks for course: {course.name}", curses.A_BOLD)
    stdscr.addstr(3, 0, f"{'Student ID':<15} | {'Name':<20} | {'Mark':<5}")
    stdscr.addstr(4, 0, "-" * 45)
    
    row = 5
    for s in students_list:
        if cid in s.marks:
            stdscr.addstr(row, 0, f"{s.student_id:<15} | {s.name:<20} | {s.marks[cid]:<5}")
            row += 1
            
    stdscr.addstr(row + 2, 0, "Press any key to return.")
    stdscr.getch()