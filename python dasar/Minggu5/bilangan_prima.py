n = 30

for i in range(2,n,1):
    prima=True
    for j in range(2,i,1):
        if(i%j==0):
            prima=False
    if (prima==True):
        print(i)