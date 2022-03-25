def binary(n):
    bin=""
    n=int(n)
    while(n!=0):
        bin=str(n%2)+bin
        n=n//2
    return bin
def dec(n):
    dec=0
    j=len(n)-1
    for i in n:
        dec+=int(i)*2**j
        j-=1
    return dec
def length(a,b):
    if len(a)>len(b):
        b="0"*(len(a)-len(b))+b
    elif len(b)>len(a):
        a="0"*(len(b)-len(a))+a
    return a,b
def Xor(a,b):
    a=binary(a)
    b=binary(b)
    AList,BList=length(a,b)
    a=AList
    b=BList
    result=""
    for i in range(len(a)):
        if(a[i]=="0" and b[i]=="0") and (a[i]=="1" and b[i]=="1"):
            result=result+"0"
        else:
            result=result+"1"
    return result
def Or(a,b):
    a=binary(a)
    b=binary(b)
    AList,BList=length(a,b)
    a=AList
    b=BList
    result=""
    for i in range(len(a)):
        if(a[i]=="0" and b[i]=="0"):
            result=result+"0"
        else:
            result=result+"1"
    return result
def And(a,b):
    a=binary(a)
    b=binary(b)
    AList,BList=length(a,b)
    a=AList
    b=BList
    result=""
    for i in range(len(a)):
        if(a[i]=="0" or b[i]=="0"):
            result=result+"0"
        else:
            result=result+"1"
    return result
    
    
    
def main():
    a=input("enter first no.")
    b=input("enter second no.")
    AND=And(a,b)
    OR=Or(a,b)
    XOR=Xor(a,b)
    print("and of",a,",",b,"is",dec(AND))
    print("or of",a,",",b,"is",dec(OR))
    print("Xor of",a,",",b,"is",dec(XOR))

if __name__=="__main__":
    main()
