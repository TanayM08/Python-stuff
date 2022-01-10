#program to calculate simple interest
def si(p ,n ,r):
    si=(p*n*r)/100

p=float(input('Enter the principal amount\n'))
n=float(input('Enter the time amount\n'))
r=float(input('Enter the rate of interest\n'))

si=si(p, n, r)
print('your simple interest is',si)
