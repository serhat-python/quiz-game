class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print(f"You're right!")
        else:
            print(f"You're wrong.")
        print(f" Current score: {self.score}/{self.question_number}")
        print(f"Correct answer: {answer}")
        print("\n")

    def end(self):
        print("You've completed the quiz ")
        print(f"Your final score: {self.score}/{len(self.question_list)}")