def Sum_of_digits(n):
    """function to find the sum of the digits."""
    sum = 0
    while (n!=0):
        sum = sum+(n%10)
        n = n//10
    print('Sum of digits of numberis:',sum)

def main():
    again= 'y'
    while again.lower()=='y':
        a= int(input("Enter the number to find the sum of digits: "))
        assert a>=0
        Sum_of_digits(a)
        print()
        again=input("Do you want to calculate the sum of digits again.(y/n):")
    print('Bye!!')

if __name__=="__main__":
    main()
