#=============================================================================
#    Program Name : Display Factors of a Number
#    Description  : Accept a number and display all its factors.
#    Function     : DisplayFactor()
#=============================================================================

class Display:

    iNo = 0

    def __init__(self,A):
        self.iNo = A

    def Chk_Factors(self):

        iCnt = 1

        print("Factors of f{iNo} Are : ")
        for iCnt in range(1,self.iNo +1):

            if(self.iNo % iCnt == 0):
                print(iCnt)

def main():

    iValue1 = 0

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    dobj.Chk_Factors()


if __name__ == "__main__":
    main()





