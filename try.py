
user_input = input("Enter something: ")

# try:

#     number = float(user_input)
#     print(f"Great! '{user_input}' is a valid number.")
# except ValueError:
#     print(f"Oops! '{user_input}' is not a valid number.")


try:
    if not user_input.isnumeric():
        raise ValueError("i/p not valid")
    else :
        print(f"Great! '{user_input}' is a valid number.")

except ValueError as e:
    print(e)