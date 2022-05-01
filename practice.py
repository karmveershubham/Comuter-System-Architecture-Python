T=int(input())
res=[]
for i in range(T):
	N=int(input())
	str=input()
	S=str.lower()
	if len(set(S))==len(S):
		res.append(1)
	else:
		res.append(0)

for i in range(T):
    print(res[i])

