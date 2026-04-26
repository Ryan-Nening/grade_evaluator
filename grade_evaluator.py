import tkinter
from tkinter import filedialog, font, messagebox

class GradeEvaluatorGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("GWA Evaluator Pro")
        self.main_window.geometry("400x350")
        self.main_window.configure(bg="#2c3e50")

    def build_user_interface(self):
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        normal_font = font.Font(family="Helvetica", size=11)
        result_font = font.Font(family="Helvetica", size=14, weight="bold")

        self.title_label = tkinter.Label(self.main_window, text="🏆 GWA Evaluator Pro", font=title_font, bg="#2c3e50", fg="#f1c40f")
        self.title_label.pack(pady=(20, 10))

        self.instruction_label = tkinter.Label(self.main_window, text="Upload student records to find the top rank.", font=normal_font, bg="#2c3e50", fg="#ecf0f1")
        self.instruction_label.pack(pady=5)

        self.evaluate_button = tkinter.Button(self.main_window, text="📂 Load Student Data", font=normal_font, bg="#3498db", fg="#ffffff", activebackground="#2980b9", activeforeground="#ffffff", relief="flat", cursor="hand2", command=self.find_highest_grade)
        self.evaluate_button.pack(pady=15, ipadx=10, ipady=5)

        self.result_frame = tkinter.Frame(self.main_window, bg="#34495e", bd=2, relief="groove")
        self.result_frame.pack(pady=10, padx=20, fill="x", ipady=15)

        self.student_name_label = tkinter.Label(self.result_frame, text="Top Student: --", font=result_font, bg="#34495e", fg="#2ecc71") 
        self.student_name_label.pack(pady=5)

        self.gwa_label = tkinter.Label(self.result_frame, text="GWA: --", font=result_font, bg="#34495e", fg="#f1c40f") 
        self.gwa_label.pack(pady=5)   

    def find_highest_grade(self):
        target_file_name = filedialog.askopenfilename(title="Select Students File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        
        if target_file_name != "":
            try:
                student_file = open(target_file_name, "r")
                top_student_name = "None"
                highest_grade_value = 5.0 
                
                for current_line in student_file:
                    if current_line.strip() == "":
                        continue 
                        
                    line_parts = current_line.strip().split(",")
                    student_name = line_parts[0].strip()
                    student_grade = float(line_parts[1].strip())
                    
                    if student_grade < highest_grade_value:
                        highest_grade_value = student_grade
                        top_student_name = student_name
                
                student_file.close()
                
                self.student_name_label.config(text="Top Student: " + top_student_name)
                self.gwa_label.config(text="GWA: " + str(highest_grade_value))
                
            except Exception:
                messagebox.showerror("File Error", "Could not process file. Ensure data is formatted as: Name, Grade")

    def run_application(self):
        self.build_user_interface()
        self.main_window.mainloop()        
