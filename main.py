# main.py
import functions
from data import countries_capitals



def main():
    print("Welcome to the Country Capital Quiz!")
    game = functions.CountryCapitalGame(countries_capitals)
    game.play_multiple_times()

if __name__ == "__main__":
    main()