def Sum_series(n):

    s=n
    sum=0
    while (n>0):
        sum+=n
        n-=1   
    print (f'sum of first {s} positive  integers: {sum} ' )

def main():
    n=int(input('Enter the nth number for the series.'))
    assert n>=0
    Sum_series(n)

if __name__=='__main__':
    main()

