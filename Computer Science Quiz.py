import tkinter as tk
import requests
import html
import random

class ComputerScienceQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Science Quiz")

        self.score = 0
        self.total_questions = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=5)

        self.options = []
        for i in range(4):
            option = tk.Button(self.options_frame, text="", font=("Arial", 12), wraplength=200, command=lambda i=i: self.select_option(i))
            option.grid(row=0, column=i, padx=5)
            self.options.append(option)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.fetch_question()

    def fetch_question(self):
        response = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
        if response.status_code == 200:
            data = response.json()
            question_data = data['results'][0]
            self.current_question = html.unescape(question_data['question'])
            self.correct_answer = html.unescape(question_data['correct_answer'])
            self.options_list = [html.unescape(option) for option in question_data['incorrect_answers']]
            self.options_list.append(self.correct_answer)
            random.shuffle(self.options_list)
            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.options[i].config(text=self.options_list[i])
            self.feedback_label.config(text="")
        else:
            self.feedback_label.config(text="Failed to fetch question. Please try again.")

    def select_option(self, index):
        selected_option = self.options_list[index]
        if selected_option == self.correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")
        self.total_questions += 1
        self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
        self.fetch_question()

root = tk.Tk()
app = ComputerScienceQuiz(root)
root.mainloop()
