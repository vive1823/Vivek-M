#3

while True:
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        a = a - 1 
    i = 1
    count = 0
    while count < a:
        print(i, end=", " if count < a - 1 else "\n")
        i += 2
        count += 1
    cont = input("\n To continue Enter 'yes' if not enter 'no': ").strip().lower()
    if cont != "yes":
        print("Thank you for using the odd number generator!")
        break
