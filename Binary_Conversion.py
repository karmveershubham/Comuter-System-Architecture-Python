def Binary(n):
    i=0
    decimal=0
    dec=0
    while(n!=0):
        dec=n%10
        decimal = decimal + dec * pow(2, i)
        n=n//10
        i=i+1
    print(decimal)


"""
    binary=""
    n=5
    while(n):
        frac_val *=2
        frac_bit= int(frac_val)
        if (frac_bit==1):
            frac_val-= frac_bit
            binary +='1'
        else:
            binary += '0'
        n -= 1
    return binary
"""

def main():
    again='y'
    while again.lower()=="y":
        a=int(input('Enter the Binary  number to convert into decimal number '))
        assert a>=0
        lis=[ch for ch in str(a)]
        if "1" or "0" in lis:
            Binary(a)
        else:
            print("Enter correct Binary number include only 1 and 0") 
        again=input('Do you want to convert other binary number.(y/n):')
    print('Bye')

if __name__=='__main__':
    main()
        
    
