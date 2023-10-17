class Quizz():
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_l = question_list

    def next_question(self):
        c_q = self.question_l[self.question_no]
        give_answer = input(f"Q {self.question_no + 1} : {c_q.text} (True or False) ")
        self.question_no += 1
        self.check_answer(give_answer, c_q.answer)

    def still_has_q(self):
        return self.question_no < len(self.question_l)

    def check_answer(self, give_answer, answer):
        if give_answer.lower() == answer.lower():
            print("You got it right !!!!")
            self.score += 1
        else :
            print("Thats wrong !!!")
        print(f"The correct answer is {answer}")
        print(f"Your score is {self.score}/{self.question_no}")
        print("\n")

