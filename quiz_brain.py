import requests
class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = []
        self.score = 0
        
        #Api used to fetch questions
    def fetch_question(self):
        url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean'
        response = requests.get(url)
        data = response.json()
        self.question_list = data['results']
        
        
        
    
    def still_have_question(self):
        return self.question_number < len(self.question_list)
            
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question['question']} (True/False)? : ").strip().capitalize()
        self.check_answer(user_answer,current_question['correct_answer'])
        
    def check_answer(self,user_answer,correct_answer):
        
        # Check if the answer is correct
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        
        # Provide feedback
        print(f"The Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    