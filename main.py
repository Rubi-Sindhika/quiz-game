from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []   # Stores the list of question objects
for item in question_data:   # Creates question object for each dictionary from data and appends it to a list
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)


my_quiz = QuizBrain(question_bank)
while my_quiz.still_has_questions():
    my_quiz.next_question()

my_quiz.final_score()
