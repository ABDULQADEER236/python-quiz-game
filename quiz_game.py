# ----------------------------------------
# Simple Quiz Game in Python
# ----------------------------------------

# Step 1: Create a list of quiz questions
# Each question is a dictionary with the question, options, and correct answer
quiz_questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Islamabad", "B. Karachi", "C. Lahore", "D. Quetta"],
        "answer": "A"
    },
    {
        "question": "Which language is used for AI programming?",
        "options": ["A. C++", "B. Python", "C. Java", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["A. Elon Musk", "B. Steve Jobs", "C. Bill Gates", "D. Mark Zuckerberg"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    }
]

# Step 2: Initialize score
score = 0

# Step 3: Display welcome message
print("Welcome to the Quiz Game!")
print("Answer the following questions by typing A, B, C, or D.\n")

# Step 4: Loop through each question
for i, q in enumerate(quiz_questions, start=1):
    print(f"Q{i}: {q['question']}")  # Display the question
    
    # Print all options
    for option in q['options']:
        print(option)
    
    # Get user input
    user_answer = input("Your answer: ").upper()  # Convert input to uppercase to match
    
    # Check answer
    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1  # Increase score if correct
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

# Step 5: Display final score
print("Quiz Completed!")
print(f"Your Final Score: {score} out of {len(quiz_questions)}")

# Step 6: End Program
print("Thanks for playing the Quiz Game 🎉")
