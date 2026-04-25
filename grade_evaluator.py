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
