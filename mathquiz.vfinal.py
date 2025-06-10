import random

# yes no checker
def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:
        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def run_quiz(generate_question_func, num_rounds):
    history = []
    correct_count = 0

    print(f"\n Math quiz: {num_rounds} questions ")
    for i in range(1, num_rounds + 1):
        question, answer = generate_question_func()
        print(f"\nQuestion {i}: What is {question}?")

        user_answer = int_check("Your answer: ")

        if user_answer == answer:
            print("✅ Correct!")
            history.append(f"Question {i}: {question} = {answer}, you were Correct!")
            correct_count += 1
        else:
            print(f"❌ Incorrect. The correct answer was {answer}.")
            history.append(f"Question {i}: {question} = {answer}, you wrote {user_answer}, Incorrect")




    print(f"\n🎯 You got {correct_count} out of {num_rounds} correct.")
    return history



# Displays instructions/
def instructions():
    print('''
**** instructions! ****
choose the number of rounds (or infinite mode)
and answer each question carefully

Good Luck!
    ''')

# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def generate_question():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(operators)
    correct_answer = 0

    # keep the division clean
    if op == '/':
        correct_answer = num1
        num1 = num1 * num2

    question = f"{num1} {op} {num2}"

    if op == '+':
        correct_answer = num1 + num2
    if op == '-':
        correct_answer = num1 - num2
    if op == '*':
        correct_answer = num1 * num2


    return question, correct_answer


operators = ['+', '-', '*', '/']
q_num = 0
q_history = []

# Main
print("🎮 Welcome to The Math Quiz!")

want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()
else:
    if want_instructions == "no":
        print("You said no")

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many questions would you like? Push <enter> for infinite mode: ")
if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 100

if q_num < num_rounds:
    q_history = run_quiz(generate_question, num_rounds)

    # todo get user input (int checker), evaluate, store history


want_hist = yes_no("do you want to see your history of the quiz")
if want_hist == "yes":
    for item in q_history:
        print(item)
else:
    print("good bye")



