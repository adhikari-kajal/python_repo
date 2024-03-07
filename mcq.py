questions = [
    "What is the capital of France?",
    # "What is the largest planet in our solar system?",
    # "Which is the closest star to Earth?",
    # "What is the chemical symbol for water?",
    # "Who wrote 'Romeo and Juliet'?"
]

options = [
    ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
    # ["A. Mars", "B. Jupiter", "C. Saturn", "D. Earth"],
    # ["A. Proxima Centauri", "B. Sirius", "C. Alpha Centauri", "D. Sun"],
    # ["A. H", "B. W", "C. H2O", "D. O"],
    # ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. J.K. Rowling"]
]

answers = ["B", "B", "D", "C", "A"]

# Initialize the score variable
score = 0

# Display the questions and options
for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ")

    # Check if the user's answer is correct
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", answers[i])

# Display the final score
print("Quiz completed!")
print("Your score:", score, "out of", len(questions))