#2  odd Number series
 
while True:
    a = int(input("Enter a Number: "))
    i = 1
    for j in range(a):
        if j == a - 1:
            print(i, end="")
        else:
            print(i, end=", ")
        i += 2

    cont = input("\n next series(yes/no)?: ").strip().lower()
    if cont != "yes":
        print("Thank you for using the odd number generator!")
        break
