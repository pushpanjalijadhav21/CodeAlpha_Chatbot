from datetime import datetime

def show_help():
    print("\nAvailable Commands:")
    print("  hello")
    print("  how are you")
    print("  what is your name")
    print("  who made you")
    print("  date")
    print("  time")
    print("  calculator")
    print("  help")
    print("  bye\n")


def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")
    except ValueError:
        print("Please enter valid numbers.")


def chatbot():
    print("=" * 45)
    print("      Welcome to Python ChatBot")
    print("=" * 45)
    print("Type 'help' to see all commands.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user == "i am fine":
            print("Bot: Glad to hear that!")

        elif user == "what is your name":
            print("Bot: My name is Python ChatBot.")

        elif user == "who made you":
            print("Bot: I was created using Python.")

        elif user == "date":
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "time":
            print("Bot:", datetime.now().strftime("%I:%M:%S %p"))

        elif user == "calculator":
            calculator()

        elif user == "help":
            show_help()

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry! I don't understand that command.")


chatbot()