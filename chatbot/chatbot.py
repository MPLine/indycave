from scout.scout import Scout
from .questions import QUESTIONS


class Chatbot:

    def __init__(self):
        self.questions = QUESTIONS
        self.current_question = 0
        self.requirements = {}
        self.scout = Scout()

    def get_current_question(self):
        if self.current_question >= len(self.questions):
            return None

        return self.questions[self.current_question]

    def process_answer(self, answer):

        question = self.get_current_question()

        if question is None:
            return self.get_results()

        self.requirements[question["key"]] = answer

        self.current_question += 1

        if self.current_question >= len(self.questions):
            return self.get_results()

        return self.get_current_question()

    def get_results(self):
        return self.scout.find_publishers(
            self.requirements
        )