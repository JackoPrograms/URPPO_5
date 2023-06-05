# Adds adds two numbers
def add(x, y):
    return x + y

# Subtract subtracts two numbers
def subtract(x, y):
    return x - y

# Multiply multiplies two numbers
def multiply(x, y):
    return x * y

# Divide divides two numbers
def divide(x, y):
    return x / y

def run():
    print("Select listed operation:\n 1) Add\n 2) Sub\n 3) Mult\n 4) Div\n")

    while True:
        choice = input("Enter your choice: ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter your first operation number: "))
                num2 = float(input("Enter your second operation number: "))
            except ValueError:
                print("Invalid input. 500 error. Try again.")
                continue

            if choice == '1':
                print(num1, " + ", num2, "   = ", add(num1, num2))

            elif choice == '2':
                print(num1, " - ", num2, "   = ", subtract(num1, num2))

            elif choice == '3':
                print(num1, " * ", num2, "   = ", multiply(num1, num2))

            elif choice == '4':
                print(num1, " / ", num2, "   = ", divide(num1, num2))

        is_need_to_continue = input("Perform another operation? (y/n): ")
        if is_need_to_continue == "n":
            break
        else:
            print("Invalid Input. Error.")

if __name__ == "__main__":
    run()