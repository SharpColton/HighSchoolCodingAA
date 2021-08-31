def GetAnswer():
    try:
        keepGoing = 0
        yes = ['y', 'yes', 'Y', 'Yes']
        no = ['n', 'no', 'N', 'No']
        x = str(input("Say yes or no :"))
        if x in yes:
            print("Your answer is yes")
            return keepGoing
        elif x in no:
            keepGoing = 1
            return keepGoing
            print("Your answer is no")
    except NameError:
        print("Invalid input")