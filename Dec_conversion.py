def Binary_int(int_val):
    binary=""
    while int_val>0:
        rem=int_val%2
        binary=str(rem)+binary
        int_val=int_val//2
    return binary

def Binary_frac(frac_val):
    binary=0
    count=0
    while (frac_val!=0 and count<=5):
        s=frac_val*2
        num=int (s)
        frac_val=s-num
        binary=binary*10 +num
        count+=1
    binary=binary*pow(10,-count)
    return str(binary) 


def Octal_int(num):
    octal=""
    while num>0:
        rem=num%8
        octal=str(rem)+octal
        num=num//8 
    return octal


def Octal_frac(frac_val):
    octal=0
    count=0
    while(frac_val!=0 and count<=5):
        s=frac_val*8
        num=int(s)
        frac_val=s-num
        octal=octal*10 +num
        count+=1
    octal=octal*pow(10,-count)
    return str(octal)


def Hexad_int(num):
    hexad=""
    while num>0:
        rem=num%16
        if rem<10:
            hexad=str(rem)+hexad
        else:
            hexad=chr(rem+55)+hexad
        num=num//16
    return hexad

def Hexad_frac(frac_val):
    hexad=""
    count=0
    while(frac_val!=0 and count<=5):
        s=frac_val*16
        num=int(s)
        if (num>=0 and num<=9): 
            hexad+=str(num)
        else:
            hexad+=chr(num+55)
        frac_val=s-int(s)
        count+=1
    return hexad


def main():
    print('MENU!\nwelcome! select a Choice.\n')
    print('1.Convert Decimal to Binary')
    print('2.Convert Decimal to Octal')
    print('3.Convert Decimal to Hexadecimal\n')

    n='y'
    while n.lower()=='y':
        a=int(input('select option:'))

        if a==1:
            num=float(input("Enter a number."))
            int_val=int(num)
            frac_val=num-int(num)
            result=float(Binary_int(int_val))+float(Binary_frac(frac_val))
            print(result)
            
        elif a==2:
            num=float(input("Enter a number."))
            int_val=int(num)
            frac_val=num-int(num)
            result=float(Octal_int(int_val))+float(Octal_frac(frac_val))
            print(result)

        elif a==3:
            num=float(input("Enter a number."))
            int_val=int(num)
            frac_val=num-int(num)
            result=Hexad_int(int_val)+"."+Hexad_frac(frac_val)
            print(result)
            
        else:
            print("Invalid Option")

        n=input('Do you want to continue?(y/n):')
        print()
    print('BYE!')
        
if __name__=='__main__':
    main()
