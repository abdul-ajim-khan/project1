
num = int((input("Enter a number: ")))
k=2*num+1
for a in range(k,1,-1):
    w=""
    for b in range(a-1):
        if(a%2==0):
            w+="*"
    if(w):
        print(w)
    else:
        continue