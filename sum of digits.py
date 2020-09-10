def sum_digits(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int (input("enter a value:"))
print(sum_digits(n))

