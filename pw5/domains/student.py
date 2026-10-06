import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {} # format {course_id: mark}
        self.gpa = 0.0

    def calculate_gpa(self, courses_list):
        if not self.marks:
            self.gpa = 0.0
            return self.gpa
            
        marks_array = []
        credits_array = []
        
        # Iterate over courses the student has marks for to get marks and credits
        for course_id, mark in self.marks.items():
            marks_array.append(mark)
            # Find the credits of the corresponding course
            for course in courses_list:
                if course.course_id == course_id:
                    credits_array.append(course.credits)
                    break

        # Convert lists to numpy arrays
        np_marks = np.array(marks_array)
        np_credits = np.array(credits_array)
        
        # Calculate GPA: Weighted average
        gpa = np.average(np_marks, weights=np_credits)
        
        # Round GPA down to 1-digit decimal
        self.gpa = math.floor(gpa * 10) / 10.0
        return self.gpa