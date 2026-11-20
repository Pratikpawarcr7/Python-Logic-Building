#=====================================================================================
#    Program Name : Check Divisibility by 3 & 5
#
#    Description :
#    Accept a number from the user and check whether
#    it is divisible by 5 using a Boolean function.
#
#    Function Name : CheckDivisible()
#
#    Return Type : bool
#=======================================================================================

class Display():

    iNo = 0

    def __init__(self,A):
        self.iNo = A

    def Chk_Divisible(self):

        if(self.iNo % 3 == 0 and self.iNo % 5 == 0):
            return True
        else:
            return False

def main():

    print("Enter the Number : ")
    iValue = int(input())

    dobj = Display(iValue)

    iRet = dobj.Chk_Divisible()

    if(iRet == True):
        print(iValue,"is Divisible by 3 and 5")
    else:
        print(iValue,"is Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()