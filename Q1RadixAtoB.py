import fractions


def split_it(number):  #split integer and fractional part.

    number = str(number)
    Nlist = number.split(".")
    if len(Nlist)==2:
        return Nlist
    else:
        return Nlist + ["0"]
    

def to_decimal(num1,num2,base1):    #num1 and num2 are numbers before and after decimal point respectively

    if base1==10:
        if num2=="0": 
            return num1
        else:
            return num1 + "." + num2
        
    else:
        int_part = 0
        j=0                
        for i in num1[::-1]:
            ord_no = ord(i)
            if ord_no in range(ord('0'),ord('9')+1):
                int_part  += int(i)*base1**j
                j += 1
            else:
                int_part += (ord(i)-55)*base1**j
                j += 1

        frac = 0
        j = -1
        for i in num2:
            ord_no = ord(i)
            if ord_no in range(ord('0'),ord('9')+1):
                frac  += int(i)*base1**j
                j -= 1
            else:
                frac += (ord(i)-55)*base1**j
                j -= 1

        return int_part+frac
    
    
def to_base(num1,num2,base2):
    if base2 == 10:
        if num2 == "0":
            return num1
        else:
            return num1+"."+num2

    num1=int(num1)
    int_part=""
    
    while(num1/base2 != 0):
        rem = num1%base2
        if rem < 10:
            int_part = str(rem) + int_part
        else:
            int_part = chr(rem+55) + int_part            
        num1 //= base2

    if num2 == "0":
        return int_part
    else: 
        frac =" "
        len2 = len(num2)
        num2=int(num2)
        while(num2 != 0):
            num2 = num2*base2
            if len(str(num2)) == len2:
                frac = frac + "0"
            else:
                if( len(str(num2)[:-len2]) > 1 ):
                    
                    char = chr( int(str(num2)[:-len2]) + 55)
                    frac = frac + char
                    num2 = int(str(num2)[-len2:])
                else:
                    frac = frac + str(num2)[0]
                    num2 = int(str(num2)[1:])
            if len(frac)>10:
                break

        return int_part+"."+frac

def base_to_base(number1,base1,base2):                 # number1 => number2 => number3 => finalNum

    if base1==base2:
        return number1
    else:
        Nlist = split_it(number1)
        num = Nlist[0]
        frac = Nlist[1]
        number2 = to_decimal(num,frac,base1)

        Nlist = split_it(number2)
        num = Nlist[0]
        frac = Nlist[1]

        number3 = to_base(num,frac,base2)

        return number3

def main():

    while(True):        
        print("Convert Number from one BASE to another BASE")

        while(True):
            
            base1 = int(input("\nEnter the Base of number.: "))
            if(base1<=1):
                print("INVALID Base, Please Enter a positive integer greater than 1.")
                continue
            elif(base1>1):
                break

        number=input("Enter the number.: ")
        if (number[0]=="-" or number[0] == "." or number.count(".")>1):
            print("Invalid Number, please Enter a positive real number.")
            continue
        else:
    
            if base1<10:
                Range = [ord(str(i)) for i in range(base1)]
            else:
                Range = [ord(str(i)) for i in range(10)] + [65+i for i in range(base1-10)]
                
            number1 = str(number)
            valid = 0
            for i in number1:
                if (i=='.'):
                    continue
                elif (ord(i) in Range):
                    valid = 1
                else:
                    valid = 0
                    break

            if(valid==0):
                print("INVALID Number for base ",base1)
                continue

        while(True):
            
            base2=int(input("Enter the Second BASE "))
            if (base2<=1):
                print("INVALID base ,Please Enter a positive integer base greater than 1")
                continue
            elif(base2>1):
                break

        finalNum = base_to_base(number1,base1,base2)

        print("Number of required base ",base2," is.: ", finalNum )
        

        c=input("\nDo you want to continue.: ")
        if(c.lower()!='y'):
            print("Bye!")
            break
            
if __name__=="__main__":
    main() 
