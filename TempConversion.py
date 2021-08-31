def GetTempConvert(calcTemp):
    while True:
        try:
            endloop = True
            #calcTemp = 0
            Flist = ['F','f','Fahrenheit','fahrenheit']
            Clist = ['C','c','Celsius','celsius']
            print('Please Enter F or C')
            tempType = str(input('Is The Temperature Above In Fahrenheit or Celsius: '))

            if tempType in Flist:
                #print('FFF'+tempType)   #Testing Only
                endloop = False
                calcTemp = ((calcTemp - 32)*(5/9))
                return round(calcTemp,1)
                break;
            elif tempType in Clist:
                #print('CCC'+tempType)  #Testing Only
                endloop = False
                calcTemp = (((9/5)*calcTemp)+ 32)
                return round(calcTemp,1)
                break;
            else:
                print('Please Enter a Valid Response')
        except NameError:
            print("Invalid input")