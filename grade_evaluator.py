import tkinter
from tkinter import filedialog

class GradeEvaluatorGui:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("GWA Evaluator Dashboard")
        self.main_window.geometry("350x200")

    def build_user_interface(self):
        self.instruction_label = tkinter.Label(self.main_window, text="Upload students file to find the top rank:")
        self.instruction_label.pack()
        self.evaluate_button = tkinter.Button(self.main_window, text="Load Data", command=self.find_highest_grade)
        self.evaluate_button.pack()

    def build_user_interface(self):
        self.instruction_label = tkinter.Label(self.main_window, text="Upload students file to find the top rank:")
        self.instruction_label.pack()
        self.evaluate_button = tkinter.Button(self.main_window, text="Load Data", command=self.find_highest_grade)
        self.evaluate_button.pack()
        self.result_label = tkinter.Label(self.main_window, text="\nTop student will appear here", font=("Arial", 12, "bold"))
        self.result_label.pack()

    def find_highest_grade(self):
        target_file_name = filedialog.askopenfilename(title="Select Students File")
        if target_file_name != "":
            student_file = open(target_file_name, "r")
            top_student_name = "None"
            highest_grade_value = 5.0
            for current_line in student_file:
                line_parts = current_line.strip().split(",")
                student_name = line_parts[0].strip()
                student_grade = float(line_parts[1].strip())
                if student_grade < highest_grade_value:
                    highest_grade_value = student_grade
                    top_student_name = student_name
            student_file.close()
            display_text = "Top Student: " + top_student_name + "\nGWA: " + str(highest_grade_value)
            self.result_label.config(text=display_text)        
