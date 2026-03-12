def ask_question(num1, num2):
    answer = num1 + num2
    user = int(input(f"What is {num1} + {num2}? "))

    if user == answer:
        print("Correct ✅")
        return 1
    else:
        print("Wrong ❌")
        return 0


score = 0

score += ask_question(2,3)
score += ask_question(5,7)
score += ask_question(10,4)

print(f"\nFinal Score: {score}/3")