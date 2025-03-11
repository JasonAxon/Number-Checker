#check section
def check_number(num):
    x = abs(int(num))
    if x % 2 == 0:
        print(num + " is an Even number.")
    else:
        print(num + " is an Odd number.")

#input section
def check():
    a = input("Give me a number to check if it is an Even or an Odd number. >> ")
    check_number(a)

#start
check()

#loop section
while True:
    continueq = input("Still got numbers to check? Y/N >> ")
    if continueq == "Y":
        check()
    else:
        print("Ok, bye.")
        break