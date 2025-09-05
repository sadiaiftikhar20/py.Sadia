#quiz game using OOP
all_questions= [
    {"question": "The Earth revolves around the Sun.", "correct_answer": "True"},
    {"question": "Python is named after a snake.", "correct_answer": "False"},
    {"question": "Water freezes at 0 degrees Celsius.", "correct_answer": "True"},
    {"question": "The capital of France is Berlin.", "correct_answer": "False"},
    {"question": "Light travels faster than sound.", "correct_answer": "True"}
]
#class of question because each question has data to store the data
class Question: #class1 
    def __init__(self, questions, answers ): 
        self.questions= questions
        self.answers = answers
#doing loop
question_bank=[]
for x in all_questions:
    question= x["question"]
    answer= x["correct_answer"]
    question_bank.append(Question(question, answer))

class QuizGame:  #class2
    def __init__(self, list_q, ):  
        self.list_q = list_q
        self.score= 0     #what is the score 
        self.q_no= 0      #what is the question number which q you are on? 
    
    def ask_q_until_all_finish(self): 
        return self.q_no < len(self.list_q) 
    
    def next_question(self):
        current_q= self.list_q[self.q_no]
        self.q_no+=1
        user_ans= input(f"Q.{self.q_no}: {current_q.questions} (True/False). ")
        self.check_ans(user_ans, current_q.answers)

    def check_ans(self,user_ans, correct_ans):
        if user_ans == correct_ans:
            print("your answer is correct")
            self.score+=1
        else:
            print("Your answer is incorrect, try again.")
        print(f"your total score is {self.score}")

final_game= QuizGame(question_bank)
while final_game.ask_q_until_all_finish():
    final_game.next_question()
