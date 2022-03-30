def isprime(x):
    for i in range(2,int(x/2) +1):
        if(x%i)==0:
            return False
    else:
         return True
def ispalindrome(x):
    rev = 0
    temp = x
    while temp>0:
        rev = (rev*10)+(temp%10);
        temp = temp//10
    if rev == x :
        return True
    else:
        return False




if __name__=="__main__":
    num1 = int(input("enter the number"))
    print(isprime(num1))
    print(ispalindrome(num1))


