import sys

# Quiz Questions and Answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. PHP", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. Bjarne Stroustrup", "D. James Gosling"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "A. Hyper Trainer Marking Language",
            "B. Hyper Text Markup Language",
            "C. Hyper Text Marketing Language",
            "D. Hyper Tool Multi Language"
        ],
        "answer": "B"
    },
    {
        "question": "Which of the following is a Python web framework?",
        "options": ["A. React", "B. Flask", "C. Angular", "D. Laravel"],
        "answer": "B"
    }
]

score = 0

# Introduction
print("📘 Welcome to the Python Quiz App!")
print("--------------------------------\n")

# Loop through questions
for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer not in ['A', 'B', 'C', 'D']:
        print("⚠️ Invalid option. Please enter A, B, C, or D.")
        sys.exit("Quiz terminated due to invalid input.")
    
    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {q['answer']}.\n")

# Final score
print("--------------------------------")
print(f"🏁 Quiz Completed! Your final score is {score} out of {len(questions)}.")

# Feedback based on performance
if score == len(questions):
    print("🏆 Outstanding! You got all questions right!")
elif score >= len(questions) * 0.6:
    print("🎯 Great job! Keep up the good work!")
else:
    print("📖 Nice try! Review and try again!")

print("--------------------------------")
