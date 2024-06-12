import random
import requests
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

# Function to fetch questions from the Open Trivia Database API
def fetch_questions():
    try:
        url = "https://opentdb.com/api.php?amount=10&type=multiple"
        response = requests.get(url)
        data = response.json()
        return data['results']
    except Exception as e:
        show_error_popup(f"Failed to fetch questions: {e}")
        return []

# Function to display a new question
def display_question():
    global current_question, options
    if questions:
        current_question = random.choice(questions)
        question_label.text = current_question['question']
        options = current_question['incorrect_answers'] + [current_question['correct_answer']]
        random.shuffle(options)
        for idx, option in enumerate(options):
            option_buttons[idx].text = option
            option_buttons[idx].background_color = (1, 1, 1, 1)  # Reset button color
    else:
        show_info_popup("No more questions available.")
        App.get_running_app().stop()

# Function to check the answer
def check_answer(selected_option):
    global score
    correct_answer = current_question['correct_answer']
    if options[selected_option] == correct_answer:
        score += 5
        show_info_popup("Correct!", True)
        option_buttons[selected_option].background_color = (0, 1, 0, 1)  # Change button color to green for correct answer
    else:
        show_info_popup(f"Wrong The correct answer is: {correct_answer}", False)
        option_buttons[selected_option].background_color = (1, 0, 0, 1)  # Change button color to red for incorrect answer

        # Highlight the correct answer
        for idx, option in enumerate(options):
            if option == correct_answer:
                option_buttons[idx].background_color = (0, 1, 0, 1)  # Change button color to green for correct answer
                break

    for btn in option_buttons:
        btn.disabled = True
    score_label.text = f"Score: {score}"

# Function to move to the next question
def next_question():
    for btn in option_buttons:
        btn.disabled = False
    display_question()

# Function to show an error popup
def show_error_popup(message):
    popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
    popup.open()

# Function to show an info popup
def show_info_popup(message, correct):
    if correct:
        color = (0, 1, 0, 1)  # Green color for correct answer
    else:
        color = (1, 0, 0, 1)  # Red color for incorrect answer

    popup = Popup(title='Info', content=Label(text=message, color=color), size_hint=(None, None), size=(400, 200))
    popup.open()

# Function to handle hover events for buttons
def on_hover_enter(btn):
    if btn.background_color != (0, 1, 0, 1) and btn.background_color != (1, 0, 0, 1):
        btn.background_color = (0.5, 0.5, 1, 1)  # Blue color when hovered
        btn.border = (1, 1, 1, 1)  # Border color
    else:
        btn.border = (1, 1, 1, 1)  # Border color

def on_hover_leave(btn):
    if btn.background_color != (0, 1, 0, 1) and btn.background_color != (1, 0, 0, 1):
        btn.background_color = (1, 1, 1, 1)  # Reset to default color when not hovered
        btn.border = (0, 0, 0, 0)  # No border
    else:
        btn.border = (0, 0, 0, 0)  # No border

class GKQuizApp(App):
    def build(self):
        # Fetch questions
        global questions, score, score_label, question_label, option_buttons, current_question, options
        questions = fetch_questions()
        score = 0
        current_question = None
        options = []

        # GUI Components
        layout = GridLayout(cols=1, padding=10, spacing=10)  # Add spacing between widgets
        
        score_label = Label(text=f"Score: {score}", font_size=25, size_hint_y=None, height=50)
        layout.add_widget(score_label)
        
        question_label = Label(text="", font_size=30, size_hint_y=None, height=150)  # Set font size to 45px for the question label
        layout.add_widget(question_label)
        
        option_buttons = []
        for i in range(4):
            btn = Button(text="", font_size=30, size_hint_y=None, height=50)  # Set font size to 30px for the option buttons
            btn.bind(on_release=lambda btn: check_answer(option_buttons.index(btn)))
            btn.bind(on_enter=on_hover_enter, on_leave=on_hover_leave)  # Bind hover events
            layout.add_widget(btn)
            option_buttons.append(btn)
        
        next_button = Button(text="NEXT", font_size=20, size_hint_y=None, height=50)
        next_button.bind(on_release=lambda btn: next_question())
        layout.add_widget(next_button)

        display_question()  # Display the first question
        return layout

if __name__ == '__main__':
    GKQuizApp().run()
