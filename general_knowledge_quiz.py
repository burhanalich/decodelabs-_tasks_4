print("===== General Knowledge Quiz =====")

score = 0

# Question 1
answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. How many continents are there? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Question 3
answer = input("\n3. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Final Score
print("\n===== Quiz Finished =====")
print("Your Final Score:", score, "/3")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep learning!")
else:
    print("Better luck next time!")