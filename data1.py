def check_prime(num):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return 0
                break  
        else:  
            return 1   
    else:  
        return 0

num = int(input())
flag=0
flag=check_prime(num)
u=num
l=num
if flag==1:
    print(num)
while flag==0:
    u=u-1
    l=l+1

    if check_prime(u):
        print(u)
        break

    if check_prime(l):
        print(l)
        break
