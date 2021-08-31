def GetTemp():
    while True:
        try:
            print('Please Enter The Temperature You Would Like Converted ')
            print('Numeric Values Only')
            temp = eval(input('Temperature To Be Converted: '))
            return temp
            break;
        except NameError:
            print ("Invalid input")