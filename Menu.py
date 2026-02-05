def user_input():
    a = int(input("please enter first number: "))
    b = int(input("please enter second number: "))
    return a,b

def menu():
    print("\n~~~Menu~~~")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = int(input("\nEnter your choice: "))
    a,b = user_input()

    if choice == 1:
        print("Add =", a+b)
    elif choice == 2:
        print("Subtract =", a-b)
    elif choice == 3:
        print("Multiply =",a*b)
    else:
        print("invalid choice")

menu()