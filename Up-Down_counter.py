import time

def binary(n): #convert decimal to binary
    bin=""
    while(n!=0):
        bin = str(n%2) + bin
        n = n//2
    return bin

def upcounter(n):
    while(True):
        print( "0"*n )
        time.sleep(2)
        for i in range (1,(2**n)):
            print("0"*(n-len(binary(i)))+binary(i))
            time.sleep(2)

def downcounter(n):
    while(True):
        for i in reversed(range(1,(2**n))):
            print("0"*(n-len(binary(i)))+binary(i))
            time.sleep(2)
        print( "0"*n )

def main():
    again='y'
    while again.lower()=="y":
        num=int(input('Enter the bits for counter.:'))
        if(num>0):
            print('\nwelcome! select a Choice.\n')
            print("1.To get Upcounter")
            print("2.To get Downcounter.\n")
        
            a=int(input('select option:'))

            if a==1:          
                upcounter(num) 
                
            elif a==2:
                downcounter(num) 

            else:
                print("Invalid Option")
        else:
            print("Enter valid Bit. should be greater than 0.")

        again=input('\nDo you want to Continue for another Value.(y/n):')
    print('Bye')

if __name__=='__main__':
    main()
