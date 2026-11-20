#============================================================================================
#    Program Name : Check Divisibility by 5
#
#    Description :
#    Accept a number from the user and check whether
#    it is divisible by 5 using a Boolean function.
#
#    Function Name : CheckDivisible()
#
#    Return Type : bool
#============================================================================================

class Display:

    def __init__(self,A):
        self.iNo1 = A

    def Chk_Divisible(self):

        if(self.iNo1 % 5 == 0):
            return True
        else:
            return False

def main():

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    iRet = dobj.Chk_Divisible()

    if (iRet == True):
        print(iValue1, "is Divisible by 5")

    else:
         print(iValue1, "is Not Divisible by 5")

if __name__ == "__main__":
    main()


