print(" We can only add and multiply")
a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Would you like to add them or multiply them: ")
d = int(a) * int(b)
e = int(a) + int(b)
if c == "Multiply" or "multiply":
    print("The answer to your question is", d)
elif c == "Add" or "add":
    print("The answer to your question is", e)
