from question_model import Question
from data import question_data
from quiz_brain import Quizz


question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

obj = Quizz(question_bank)
while obj.still_has_q():
    obj.next_question()
print("You have completed the quiz!!!")
print(f"Your score : {obj.score}/12")