n=6
ini=6
pow_n=6
p_var=1
flag=0
while n<=pow_n:
    if n==pow_n:
        flag=1
        print(1)
        break
    else:
        n=n*ini
if flag==0:
    print(0)
