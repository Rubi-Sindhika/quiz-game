class QuizBrain:
    """"""
    def __init__(self, q_list):
        self.question_number = 0
        self.qlist = q_list
        self.score = 0

    def next_question(self):
        current_question = self.qlist[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} ('True/False'): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        if self.question_number == len(self.qlist):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n" * 2)

    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score is {self.score}")
