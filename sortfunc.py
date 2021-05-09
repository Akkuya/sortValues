import gc


def sort():
    list = []  # Creates an empty list

    def checkNum():
        num1 = input("Enter how many numbers you wish to sort. ")
        try:
            # Try converting the input into an integer
            checkNum.intNum1 = int(num1)
        except ValueError:
            print("Invalid input, please try again.")
            checkNum()  # Call back

    def appendValues():
        append = input()
        try:
            appendValues.floatAppend = float(append)
        except ValueError:
            print("Invalid input, please try again.")
            appendValues()

    def sortValues():
        print("Please specify whether you want to sort it ascending or descending. (a/d)")
        sortDirection = input()
        if sortDirection == ("a"):
            list.sort()
        elif sortDirection == ("d"):
            list.sort(reverse=True)
        else:
            print("Invalid input, please try again.")
            sortValues()

    checkNum()
    for i in range(checkNum.intNum1):
        print("Please enter number " + str(i + 1) + ".")
        appendValues()
        list.append(appendValues.floatAppend)
    sortValues()
    print(list)
    del list
    gc.collect()


while True:
    sort()
