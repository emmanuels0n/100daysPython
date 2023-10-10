from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)  # I can leave also only the name
    # parameters (the second ones)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():  # if quiz still
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

