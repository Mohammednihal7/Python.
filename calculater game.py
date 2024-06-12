import tkinter as tk
from tkinter import PhotoImage
import random

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        
        # Load your own logo image
        self.logo_image = PhotoImage(file="your_logo.png")  # Replace "your_logo.png" with your image file path
        
        # Create a label to display the logo
        self.logo_label = tk.Label(root, image=self.logo_image)
        self.logo_label.pack()

        # Other widgets and functionality can be added below
        self.generate_question()

    def generate_question(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operator = random.choice(['+', '-', '*'])
        
        if self.operator == '+':
            self.answer = self.num1 + self.num2
        elif self.operator == '-':
            self.answer = self.num1 - self.num2
        else:
            self.answer = self.num1 * self.num2
        
        question_text = f"What is {self.num1} {self.operator} {self.num2}?"
        self.question_label = tk.Label(self.root, text=question_text, font=("Arial", 18))
        self.question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(self.root, font=("Arial", 16))
        self.answer_entry.pack(pady=10)
        
        self.check_button = tk.Button(self.root, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)
        
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.answer:
                self.feedback_label.config(text="Correct!", fg="green")
            else:
                self.feedback_label.config(text="Incorrect. Try again.", fg="red")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

root = tk.Tk()
app = MathQuiz(root)
root.mainloop()
