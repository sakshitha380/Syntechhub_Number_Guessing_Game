
import random

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)

best_scores = {}

while True:
    print("\nChoose Difficulty:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 500)")

    choice = input("Enter your choice: ")

    if choice == "1":
        difficulty = "Easy"
        max_number = 50
    elif choice == "2":
        difficulty = "Medium"
        max_number = 100
    elif choice == "3":
        difficulty = "Hard"
        max_number = 500
    else:
        print("Invalid choice! Select 1, 2 or 3.")
        continue

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > max_number:
                print(f"Enter a number from 1 to {max_number}.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Higher! Try again.")
        elif guess > secret_number:
            print("Lower! Try again.")
        else:
            print("\nCongratulations! You guessed it!")
            print("Attempts:", attempts)
            break

    # Update best score for this difficulty
    if (difficulty not in best_scores or
            attempts < best_scores[difficulty]):
        best_scores[difficulty] = attempts
        print("New best score!")

    print("\nBest Scores:")
    for level, score in best_scores.items():
        print(f"{level}: {score} attempts")

    replay = input("\nPlay again? (y/n): ").lower()

    if replay != "y":
        print("\nThank you for playing!")
        print("Goodbye!")
        break