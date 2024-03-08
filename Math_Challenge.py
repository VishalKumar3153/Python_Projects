import random
import time
operators=["+","-","*"]
min_operand=2
max_operand=15
no_of_questions=10
def generate():
    operand1=random.randint(min_operand,max_operand)
    operand2=random.randint(min_operand,max_operand)
    operator=random.choice(operators)
    question=(str(operand1)+operator+str(operand2))
    answer=eval(question)
    return question,answer
wrong=0
input("Press enter to start!")
print("---------------------------")
str_time=time.time()
for i in range(no_of_questions):
    question,answer=generate()
    while True:
        guess=input("Question"+ str(i+1)+": " +str(question) + "= ")
        if guess == str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time-str_time,2)
print("---------------------------")
print("Nice Work :) You finished in",total_time,"seconds!")





