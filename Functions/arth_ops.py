def arithmetic_ops():
    inp = int(
        input(
            "Select the operation you want to perform :\n 1. Additon\n 2. Subtraction\n 3. Multiplication\n 4. Division\n Enter your choice: "
        )
    )
    a, b = map(int, input("Enter a and b values :").split())
    match inp:
        case 1:
            print(f"Addition of {a} and {b} is {a+b}")
        case 2:
            print(f"Subtraction of {a} and {b} is {a-b}")
        case 3:
            print(f"Multiplication of {a} and {b} is {a*b}")
        case 4:
            print(f"Division of {a} and {b} is {a//b}")


arithmetic_ops()
