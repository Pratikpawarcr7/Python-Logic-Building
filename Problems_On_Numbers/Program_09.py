#======================================================================
#   Write a Python program to display numbers from 1 to N.
#======================================================================

class Display:

    iNo1 = 0

    def __init__(self,A):
        self.iNo1 = A

    def Numbers(self):

        iCnt = 0

        print("OutPut : ")

        for iCnt in range(1,self.iNo1 + 1):

            print(iCnt)

def main():

    iValue1 = 0
    
    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display(iValue1)

    dobj.Numbers()

if __name__ == "__main__":
    main()