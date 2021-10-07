#program to find largest number in a list

l=[]
for i in range(1,6):
    num=int(input('Enter your values\n'))
    l.append(num)
    
print(l)

l.sort()
print('the largest number is ',l[-1])
