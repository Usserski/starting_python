import pygame
import sys
import random

WIDTH = 800
HEIGHT = 600

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Quiz Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.questions = self.load_questions()
        self.current_question_index = 0
        self.score = 0

    def load_questions(self):
        # Przykładowe pytania
        return [
            Question("Jakie jest stolicą Polski?", ["Warszawa", "Berlin", "Paryż", "Londyn"], "Warszawa"),
            Question("Ile to 2 + 2?", ["3", "4", "5", "6"], "4"),
            Question("Który kontynent jest największy?", ["Afryka", "Azja", "Europa", "Ameryka"], "Azja"),
        ]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.check_answer(0)
                    elif event.key == pygame.K_2:
                        self.check_answer(1)
                    elif event.key == pygame.K_3:
                        self.check_answer(2)
                    elif event.key == pygame.K_4:
                        self.check_answer(3)

            self.screen.fill((255, 255, 255))
            self.display_question()
            pygame.display.flip()
            self.clock.tick(60)

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question_text = self.font.render(question.question, True, (0, 0, 0))
            self.screen.blit(question_text, (50, 50))

            for index, option in enumerate(question.options):
                option_text = self.font.render(f"{index + 1}. {option}", True, (0, 0, 0))
                self.screen.blit(option_text, (50, 100 + index * 40))

        else:
            self.display_score()

    def check_answer(self, selected_index):
        question = self.questions[self.current_question_index]
        if question.options[selected_index] == question.answer:
            self.score += 1

        self.current_question_index += 1

    def display_score(self):
        score_text = self.font.render(f"Twój wynik: {self.score}/{len(self.questions)}", True, (0, 0, 0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

if __name__ == "__main__":
    game = QuizGame()
    game.run()
