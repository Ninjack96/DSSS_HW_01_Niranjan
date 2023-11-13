import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': 
        a = n1 + n2  # Operator is corrected to `+` instead of `-`, which is not suitable here!
    elif o == '-': 
        a = n1 - n2  # Operator is corrected to `-` instead of `+`, which is not suitable here!
    else: 
        a = n1 * n2  # The statement is moved to the next line as it has a else statement!
    return p, a

def math_quiz():
    s = 0
    t_q = 3  # As the value is not suitable in reqaal life scenario , changed the flot value of `3.14` to nearest possible integar

    print("Curious to do some brain  teasers? Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers to win the quiz.")

    for _ in range(t_q):
        n1 = function_A(1, 10) 
        n2 = function_A(1, 6) 
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try : 
            useranswer = int(useranswer)
        except ValueError:
            print("Enter the correct Whole Number!")
            continue
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1 
        else:
            print(f"Better luck next time. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
