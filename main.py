from question_model import Question
from data import data
from quiz_brain import QuizBrain
from logo import logo

print(logo)


quiz = QuizBrain()
quiz.fetch_question()
question_bank = []

for question in quiz.question_list:
    ques = question['question'] 
    ans = question['correct_answer']
    
    new_question = Question(ques,ans)
    question_bank.append(new_question)
    
while quiz.still_have_question():
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")