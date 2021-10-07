#program to check if a number is a palindrome
num=int(input('Enter a number'))
rev=num
a=0
while(num>0):
    x=121%10
    print(x)
    a=a+10+x
    print(a)
    num=num/10
    print(num)
    
if reverse==a:
    print('It is a pelindrome number')
else:
    print('It is not a pelindrome number')
