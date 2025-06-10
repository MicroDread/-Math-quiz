import random

# random number quiz generator
def generate_question_1():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num1 * num2

    question1 = f"{num1} {op} {num2}"
    correct_answer = eval(question1)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question1, correct_answer


def generate_question_2():
    operations = ['+', '-', '*', '/']
    num3 = random.randint(1, 50)
    num4 = random.randint(1, 50)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num3 * num4

    question2 = f"{num3} {op} {num4}"
    correct_answer = eval(question2)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question2, correct_answer


def generate_question_3():
    operations = ['+', '-', '*', '/']
    num5 = random.randint(50, 100)
    num6 = random.randint(50, 100)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num5 * num6

    question3 = f"{num5} {op} {num6}"
    correct_answer = eval(question3)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question3, correct_answer


def generate_question_4():
    operations = ['+', '-', '*', '/']
    num7 = random.randint(100, 500)
    num8 = random.randint(100, 500)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num7 * num8

    question4 = f"{num7} {op} {num8}"
    correct_answer = eval(question4)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question4, correct_answer


def generate_question_5():
    operations = ['+', '-', '*', '/']
    num9 = random.randint(500, 1000)
    num10 = random.randint(500, 1000)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num9 * num10

    question5 = f"{num9} {op} {num10}"
    correct_answer = eval(question5)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question5, correct_answer


def run_quiz(level_name, generate_question_func, num_rounds):
    history = []
    correct_count = 0

    print(f"\n📘 Starting Level: {level_name}")
    for i in range(1, num_rounds + 1):
        question, answer = generate_question_func()
        print(f"\nQuestion {i}: What is {question}?")

        try:
            user_input = input("Your answer: ")
            user_answer = float(user_input)

            if round(user_answer, 2) == round(answer, 2):
                print("✅ Correct!")
                correct = True
                correct_count += 1
            else:
                print(f"❌ Incorrect. The correct answer was {answer}.")
                correct = False

        except ValueError:
            print(f"❌ Invalid input. The correct answer was {answer}.")
            correct = False
            user_answer = user_input

        history.append({
            "number": i,
            "question": question,
            "correct_answer": answer,
            "user_answer": user_answer,
            "correct": correct
        })

    print(f"\n🎯 You got {correct_count} out of {num_rounds} correct.")
    return history



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


# Displays instructions
def instructions():
    print('''
**** instructions! ****
To begin, choose the level of difficulty you want from 1 (easy) to 5 (extreme)
Then choose the number of rounds (or infinite mode)

Good Luck!
    ''')

# Check that users has entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# checks for num of rounds, if more than 0 (allows <enter>)
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


def level_checker(question):
    while True:

        responses = input(question).lower()


        if responses == "1" or responses == "level 1":
            return "level 1"
        if responses == "2" or responses == "level 2":
            return "level 2"
        if responses == "3" or responses == "level 3":
            return "level 3"
        if responses == "4" or responses == "level 4":
            return "level 4"
        if responses == "5" or responses == "level 5":
            return "level 5"
        else:
            print("❌ Invalid level selected.")


def main():
    print("🎮 Welcome to The Math Quiz!")

    want_instructions = yes_no("Do you want to see the instructions? ")

    if want_instructions == "yes":
        instructions()
    else:
        if want_instructions == "no":
            print("You said no")

    # Shows the user the levels
    print("1. Level 1 (Easy)")
    print("2. Level 2 (Medium)")
    print("3. Level 3 (Hard)")
    print("4. Level 4 (Very Hard)")
    print("5. Level 5 (Extreme)")

    level = level_checker("Please choose the level you want: ")

    # Ask user for number of rounds
    num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
    if num_rounds == "infinite":
        num_rounds = 999  # or any number
        # for infinite

    # Choose level and run the correct level quiz
    if level == "level 1":
        history = run_quiz("Level 1", generate_question_1, num_rounds)
    elif level == "level 2":
        history = run_quiz("Level 2", generate_question_2, num_rounds)
    elif level == "level 3":
        history = run_quiz("Level 3", generate_question_3, num_rounds)
    elif level == "level 4":
        history = run_quiz("Level 4", generate_question_4, num_rounds)
    elif level == "level 5":
        history = run_quiz("Level 5", generate_question_5, num_rounds)

    # Shows results
    correct_count = sum(1 for record in history if record["correct"])
    print(f"\n🎯 Total correct answers: {correct_count} out of {num_rounds}")

    print("\n📜 Quiz Summary:")
    for record in history:
        status = "✔️" if record["correct"] else "❌"
        print(f"Q{record['number']}: {record['question']} = {record['correct_answer']} | Your answer: {record['user_answer']} {status}")

    percentage = (correct_count / num_rounds) * 100
    print(f"\n🎯 You got {correct_count} out of {num_rounds} correct ({percentage:.2f}%)")
    print("thank you for playing, quiz by Kuzi")

if __name__ == "__main__":
    main()

