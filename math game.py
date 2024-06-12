import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Math Quiz Game')

# Load font
font = pygame.font.SysFont("comicsans", 50)
small_font = pygame.font.SysFont("comicsans", 35)

# Game variables
score = 0
question, correct_answer = "", 0
user_answer = ""
quiz_running = True

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    return question, correct_answer

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    global question, correct_answer, user_answer, score, quiz_running
    question, correct_answer = generate_question()

    while True:
        screen.fill(WHITE)

        if quiz_running:
            draw_text("Math Quiz Game", font, BLACK, screen, 280, 20)
            draw_text(f"Score: {score}", small_font, BLACK, screen, 50, 100)
            draw_text(question, font, BLACK, screen, 350, 200)
            draw_text("Your Answer: " + user_answer, small_font, BLACK, screen, 300, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            if int(user_answer) == correct_answer:
                                score += 1
                                user_answer = ""
                                question, correct_answer = generate_question()
                            else:
                                quiz_running = False
                        except ValueError:
                            user_answer = ""  # Reset user answer if it's invalid
                    elif event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]
                    elif event.unicode.isdigit() or (event.unicode == '-' and user_answer == ''):
                        user_answer += event.unicode

        else:
            draw_text("Game Over", font, RED, screen, 300, 200)
            draw_text(f"Final Score: {score}", small_font, BLACK, screen, 350, 300)
            draw_text(f"The correct answer was: {correct_answer}", small_font, BLACK, screen, 300, 350)
            draw_text("Press R to Restart or Q to Quit", small_font, BLACK, screen, 200, 400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        quiz_running = True
                        score = 0
                        question, correct_answer = generate_question()
                        user_answer = ""

        pygame.display.update()

if __name__ == "__main__":
    main()
