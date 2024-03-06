questions = [
    "What is 1 + 1? ",
    "What is the capital of France? ",
    "What color is the sky? ",
    "What is the opposite of up? ",
    "What is 2 * 3? "
]

answers = ["2", "Paris", "Blue", "Down", "6"]

score=0
for i in range(len(questions)):
    user_answer = input(questions[i])

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", answers[i])

print("Quiz completed!")
print("Your score:", score, "out of", len(questions))