import RequestingToContinue
import TempConversion
import NumTemp

answer = 0
while answer == 0:

    newTemp = NumTemp.GetTemp()
    print('-Successfully Stored-')
    print('Thank You For Your Input!')
    print('You Entered ',newTemp,' Degrees')
    finalTemp = TempConversion.GetTempConvert(newTemp)
    print(finalTemp)
    answer = RequestingToContinue.GetAnswer()
    print(answer)
else:
    print("Thank You For Using Our New Software!")