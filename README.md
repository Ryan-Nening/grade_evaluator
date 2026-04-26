# GRADE EVALUATOR

## Description
This program is an Object-Oriented Graphical User Interface (GUI) tool built with Python and `tkinter`. It functions as a professional academic dashboard that evaluates student performance. By reading a text file of students and their General Weighted Averages (GWA), the program calculates and instantly displays the top-ranking student inside a dedicated visual frame. 

*Note: The logic strictly follows a grading system where a lower numerical value (e.g., 1.00 or 1.25) represents a higher academic grade.*

## Features
* **Academic Slate Theme:** A modern, deep-blue visual interface featuring custom fonts and dynamic accent colors.
* **Result Dashboard Frame:** Outputs the winning student's data into a centralized, stylized container instead of raw text.
* **Crash Protection:** Implements `try-except` error handling. If a user uploads an improperly formatted file, the program displays a safe error message box instead of crashing the application.
* **Two-File OOP Architecture:** Strictly adheres to Object-Oriented Programming best practices by separating the class blueprint from the main execution driver.

## How to Use
1. **Prepare the Data:** Create a text file named students.txt in the same directory as the scripts. Enter student data with one student per line, separating the name and the GWA with a comma (e.g., Juan Dela Cruz, 1.50).
2.  **Run the Program:** Open your terminal or IDE and execute the main driver file:

    ``python main_program_for_grade_evaluator.py``
4. **Load the Data:** Click the "Load Student Data" button on the dashboard.
5. **Select the File:** Use the filtered file explorer to locate and select your students.txt file.
6. **View Results:** The dashboard will instantly process the data and display the top student in the result frame.
