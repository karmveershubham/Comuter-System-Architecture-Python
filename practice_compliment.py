def flip(a):
    if a=="1":
        return "0"
    elif a=="0":
        return "1"
def compliment(a):
    ones=""
    twos=""
    for i in range (len(a)):
        ones+=flip(a[i])
    ones=list(ones)
    twos=list(ones)
    
    for i in reversed(range(len(a))):
        if ones[i]=="1":
            twos[i]="0"
        elif ones[i]=="0":
            twos[i]="1"
            break
    #i-=1
    print(twos)
    #if(i==-1):
        #twos.insert(0,"1")
    ones="".join(ones)
    twos="".join(twos)
    return ones,twos
def main():
    a=input("give binary number")
    #print(type(a))
    res1,res2=compliment(a)
    print("ones compliment of",a,"is",res1)
    print("twos compliment of",a,"is",res2)
if __name__=="__main__":
    main()
