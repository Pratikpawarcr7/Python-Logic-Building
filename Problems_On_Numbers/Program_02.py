#============================================================================================================================
#    Program Name : Display Numbers up to N
#
#    Description :
#    Write a Python program to accept one integer number from the user and display all numbers from 1
#    up to the entered number using a for loop.
#
#    Function Name : Display()
#
#    Parameter : iNo - Accepts an integer number.
#
#    Logic :
#    1. Initialize the counter variable iCnt to 0.
#    2. Start the for loop from 1.
#    3. Repeat the loop until iCnt is less than
#       or equal to iNo.
#    4. Display each number using printf().
#============================================================================================================================

class Display:

    iNo1 = 0
    def __init__(self,A):
        self.iNo = A


    def Numbers(self):

        for iCnt in range(1,self.iNo+1):
            print("Jay Ganesh....")




def main():

    print("Enter the How Many Times You Want To print")
    iValue = int(input())

    dobj =  Display(iValue)

    dobj.Numbers()



if __name__ == "__main__":
    main()