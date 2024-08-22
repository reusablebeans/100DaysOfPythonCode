import calculator_art as art
def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    print(art.logo)
    should_accumulate = True
    x1 = float(input("Enter the first value:\n"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter what operation you would like to perform:\n")
        x2 = float(input("Enter the second value:\n"))
        answer = operations[operation_symbol](x1, x2)
        print(f"{x1} {operation_symbol} {x2} = {answer}")
        choice = input(f"Do you want to keep working with the value {answer} \"y\", or clear the calculator \"n\":\n")
        if choice == "y":
            x1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 25)
            calculator()

calculator()