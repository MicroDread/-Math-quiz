import random
from http.client import responses
from operator import truediv


def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)

    # don't divide by zero and keep the division clean
    if op == '/':
        num1 = num1 * num2

    question = f"{num1} {op} {num2}"
    correct_answer = eval(question)
    if op == '/':
        correct_answer = round(correct_answer, 2)

    return question, correct_answer


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

To begin, choose the number of rounds (or infinite mode)

Then play against the computer. You need to choose R (Rock), P (Paper, or S (scissors).

The rules are as follows:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <xxx> to end the game at anytime.

Good Luck!
    ''')


# Check that users have entered a valid
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
            return "level "
        if responses == "2" or responses == "level 2":
            return "level 2"
        if responses == "3" or responses == "level 3":
            return "level 3"
        if responses == "4" or responses == "level 4":
            return "level 4"
        if responses == "5" or responses == "level 5":
            return "level 5"
        else:
                print("Choose what level you want from 1 easy to 5 insane")



def main():
    print("🎮 Welcome to The Math Quiz!")

    # ask the user if they want to see the instructions and display
    # them if requested
    want_instructions = int_check(" do you want to see the instructions? ")

    # checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        instructions()

    # ask user for number of rounds / infinite mode
    num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
    while True:
        try:
            if num_rounds == "infinite":
                mode = "infinite"
                num_rounds = 100
            if num_rounds <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")


    history = []
    correct_count = 0

    for i in range(1, num_rounds + 1):
        question, answer = generate_question()
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

        # keep original text for the history
        history.append({
            "number": i,
            "question": question,
            "correct_answer": answer,
            "user_answer": user_answer,
            "correct": correct
        })

    # Show results
    print("\n📜 Quiz Summary:")
    for record in history:
        status = "✔️" if record["correct"] else "❌"
        print(f"Q{record['number']}: {record['question']} = {record['correct_answer']} | Your answer: {record['user_answer']} {status}")

    percentage = (correct_count / num_rounds) * 100
    print(f"\n🎯 You got {correct_count} out of {num_rounds} correct ({percentage:.2f}%)")

if __name__ == "__main__":
    main()

