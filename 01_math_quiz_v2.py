import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)

    # Avoid division by zero and keep division clean
    if op == '/':
        num1 = num1 * num2  # ensures it divides evenly

    question = f"{num1} {op} {num2}"
    correct_answer = eval(question)
    if op == '/':
        correct_answer = round(correct_answer, 2)  # Round division answers

    return question, correct_answer


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


def main():
    print("🎮 Welcome to The Math Quiz!")
    while True:
        try:
            # ask user for number of rounds / infinite mode
            num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

            if num_rounds == "infinite":
                mode = "infinite"
                num_rounds = 5

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
            user_answer = user_input  # keep original text for the history

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

