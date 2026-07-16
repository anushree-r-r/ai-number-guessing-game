import random
import time

# Difficulty settings
levels = [
    {"name": "Easy", "range": 50, "attempts": 10},
    {"name": "Medium", "range": 100, "attempts": 7},
    {"name": "Hard", "range": 200, "attempts": 5}
]

def get_hint(number, guess):
    diff = abs(number - guess)

    if diff == 0:
        return "Perfect!"
    elif diff <= 5:
        return "Very Hot!"
    elif diff <= 10:
        return "Hot!"
    elif diff <= 20:
        return "Warm"
    else:
        return "Cold"

def adjust_difficulty(current_level, attempts_used, max_attempts, time_taken):
    performance_score = (max_attempts - attempts_used) * 2 + (30 - time_taken)

    if performance_score > 20 and current_level < 2:
        print("AI: You're doing great! Increasing difficulty")
        return current_level + 1
    elif performance_score < 5 and current_level > 0:
        print("AI: Let's make it easier")
        return current_level - 1
    else:
        print("AI: Maintaining current level")
        return current_level

def play_game(level_index):
    level = levels[level_index]
    number = random.randint(1, level["range"])
    max_attempts = level["attempts"]

    print(f"\nLevel: {level['name']}")
    print(f"Guess a number between 1 and {level['range']}")

    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: "))
            attempts += 1

            hint = get_hint(number, guess)

            if guess == number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)

                print("\nCorrect Guess!")
                print(f"Hint: {hint}")
                print(f"Time: {time_taken} sec")

                return attempts, max_attempts, time_taken

            else:
                print(f"AI Hint: {hint}")

                if guess < number:
                    print("Try higher")
                else:
                    print("Try lower")

        except ValueError:
            print("Enter a valid number.")

    print(f"\nGame Over! Number was {number}")
    return max_attempts, max_attempts, 30  # worst performance

def main():
    print("AI Adaptive Number Guessing Game")

    level_index = 1  # Start at Medium

    while True:
        attempts_used, max_attempts, time_taken = play_game(level_index)

        level_index = adjust_difficulty(
            level_index,
            attempts_used,
            max_attempts,
            time_taken
        )

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

main()