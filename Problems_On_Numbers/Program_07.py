#===============================================================================================
#   Program Name : Display Factors of a Number
#   Description  : Accept a number and display the Addition of all its factors.
#  Function     : DisplayFactor()
#==============================================================================================

class Display:

    iNo = 0

    def __init__(self,A):
        self.iNo = A

    def Chk_Factors(self):

        iCnt = 1
        iSum = 0

        print(f"Factors of {self.iNo} Are : ")
        for iCnt in range(1,self.iNo):
       
            if(self.iNo % iCnt == 0):

                print(iCnt)

                iSum = iSum + iCnt

        return iSum
                
def main():

    iValue1 = 0
    iRet = 0

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    iRet =  dobj.Chk_Factors()

    print(f"Addition : {iRet}")


if __name__ == "__main__":
    main()



