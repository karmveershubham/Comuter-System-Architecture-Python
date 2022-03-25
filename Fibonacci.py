def Fibonacci(n):
    if  n<=0:
        print('Incorrect option')

    elif n==1:
        return 0

    elif n==2:
        return 1

    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    

def main():
    again='y'
    while again.lower()=='y':
        a= int(input('To get the nth term of febonacci seies. \nEnter the value of n:'))
        print ('The ', a, 'th term of fibonacci series is:',Fibonacci(a))
        print('Fibonacci series:')
        for i in range(1,a+1):
            print(Fibonacci(i))
        again=input('\nDo you want to print and check another value.(y/n)')
    print('Bye!')

if __name__=='__main__':
    main()

