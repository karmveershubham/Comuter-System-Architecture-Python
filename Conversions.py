# Function to return ASCII value of a character

def val(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65  + 10

# Function to convert a number from given base to decimal number

def toDeci(strr, base):

    lenn = len(strr)  # Stores the length of the string
    power = 1         # Initialize power of base
    num = 0           # Initialize result

    
    # Decimal equivalent is strr[len-1]*1 + strr[len-2]*base + strr[len-3]*(base^2) + ...
    for i in range(lenn - 1, -1, -1):

        # A digit in input number must be less than number's base
        if (val(strr[i]) >= base):  
            print("Invalid Number")
            return -1
        
        num += val(strr[i]) * power    # Update num
        power = power * base           # Update power

    return num


# Function to return equivalent character of a given value
def reVal(num):

    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)
    

# Function to convert a given decimal number to a given base
def fromDeci(base, inputNum):

    res = "" # Store the result

    # Repeatedly divide inputNum by base and take remainder
    while (inputNum > 0):

        res += reVal(inputNum % base)    # Update res
        inputNum //= base                # Update inputNum
        
    res = res[::-1]                      # Reverse the result

    return res


# Function to convert a given number
# from a base to another base
def convertBase(Number, Base1, Base2 ):

    # Convert the number from
    # Base1 to decimal
    Num = toDeci(Number , Base1)

    # Convert the number from
    # decimal to base B
    Answer = fromDeci(Base2, Num)

    # Print the result
    return Answer

def main():
    n='y'
    while n.lower()=='y':
            Base1=int(input("Enter Base for the number."))
            Base2=int(input("Enter the Base in which number convert. "))
            Number=input("Enter the number.")

            # Function Call

            Result=convertBase(Number, Base1, Base2 )

            print(f"The conversion  of the {str(Number)} into base {Base2} is {Result} " )
            
            n=input('Do you want to continue?(y/n):')
            print()
    print('BYE!')
    
if __name__=='__main__':
    main()

