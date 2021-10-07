#qn4 program to check if a number is a prime number or not

num=int(input('Enter your value\n'))

if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print('its not a prime number')
            break
    else:
        print('It is a prime number')
