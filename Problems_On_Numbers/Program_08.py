#=================================================================================
#  Program Name : Display Factors of a Number
#  Description : Accept a number and display the Perfect Number.
#  Function : DisplayFactor()
#================================================================================

class Display:

    iNo = 0
    
    def __init__(self,A):

        self.iNo = A

    def Chk_Factors(self):

        iCnt = 0
        iSum = 0

        print(f"Factors of {self.iNo} Are : ")

        for iCnt in range(1,self.iNo):

            if(self.iNo % iCnt == 0):

                print(iCnt)

                iSum = iSum + iCnt

        print(f"Addition of all Factors of {self.iNo} is : {iSum} ")

        if iSum == self.iNo:
            
            return True

        else:
            
            return False

def main():

    iValue1 = 0
    iRet = False

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    iRet = dobj.Chk_Factors()

    if iRet == True:

        print(f"{iValue1} is Perfect Number ")

    else:

        print(f"{iValue1} is Not Perfect Number ")


if __name__ == "__main__":
    main()