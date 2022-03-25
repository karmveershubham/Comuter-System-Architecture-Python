def factorial(n):
    """function to print the factorial value of the number given by user."""
    x=1
    for i in range (1,n+1):
        x=x*i
    print(x)
4


def main():
    again='y'
    while again.lower()=="y":
        a=int(input('Enter the number whose factorial is to be calculated.'))
        assert a>=0
        factorial(a)
        again=input('Do you want to calculate another fatorial.(y/n):')
    print('Bye')

if __name__=='__main__':
    main()
        
    
        
        
        
