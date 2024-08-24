class Question:
    """Creates object of question model, when text for the question and answer is passed"""
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer
