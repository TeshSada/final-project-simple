# functions.py
import random
import time

class CountryCapitalGame:
    def __init__(self, countries_capitals):
        self.countries_capitals = countries_capitals
        self.leaderboard = self.load_leaderboard()

    def display_score(self, score):
        print("Your score:", score)

    def display_correct_answer(self, country, capital):
        print(f"The correct answer is {country} with capital {capital}.")

    def display_question(self, country):
        print(f"What is the capital of {country}?")

    def get_user_input(self):
        return input("Enter your guess: ")

    def check_input(self, guess, country, capital):
        return guess.lower() == capital.lower()

    def get_random_country(self):
        country = random.choice(list(self.countries_capitals.keys()))
        capital = self.countries_capitals[country]
        return country, capital

    def update_leaderboard(self, score, time_taken, correct_answers):
        self.leaderboard.append({"score": score, "time_taken": time_taken, "correct_answers": correct_answers})
        self.leaderboard.sort(key=lambda x: x["score"], reverse=True)
        self.leaderboard = self.leaderboard[:10]

    def load_leaderboard(self):
        try:
            with open("leaderboard.txt", "r") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []

    def save_leaderboard(self):
        with open("leaderboard.txt", "w") as file:
            file.write(str(self.leaderboard))

    def play_game(self):
        start_time = time.time()
        score = 0
        attempts = 0
        correct_answers = []

        while score < len(self.countries_capitals):
            country, capital = self.get_random_country()
            self.display_question(country)
            guess = self.get_user_input()

            if self.check_input(guess, country, capital):
                print("Correct!")
                score += 1
                correct_answers.append((country, capital))
            else:
                print("Incorrect!")
                self.display_correct_answer(country, capital)
                attempts += 1

            if attempts == 3:
                print("Game Over! You've reached the maximum number of attempts.")
                break

        end_time = time.time()
        time_taken = end_time - start_time
        self.display_score(score)
        self.update_leaderboard(score, time_taken, correct_answers)
        self.save_leaderboard()
        return score, correct_answers

    def play_multiple_times(self):
        while True:
            score, correct_answers = self.play_game()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
