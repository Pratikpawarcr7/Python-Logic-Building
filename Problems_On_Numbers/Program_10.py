#============================================================================
#  Write a Python program to calculate the sum of numbers from 1 to N.
#=============================================================================

class Display:

    iNo1 = 0

    def __init__(self,A):
        self.iNo1 = A

    def Numbers(self):

        iCnt = 0
        iSum = 0

        for iCnt in range(1,self.iNo1 + 1):

            iSum = iSum + iCnt

        return iSum

def main():

    iValue1 = 0
    iRet = 0
    
    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    iRet =  dobj.Numbers()

    print(f"Addition : {iRet}")

if __name__ == "__main__":
    main()