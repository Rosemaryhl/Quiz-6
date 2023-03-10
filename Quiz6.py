#Rosemary Hoffman Quiz 6
#Problem 1
#Ctrl+C to stop
n=-1
while n<0:
    print("n is negative")

#Problem 2
#print sum of all postiive even numbers less than 12

i=2
sum=0
while i<12:
    sum+=i
    i+=2
#
#
# print("the sum of all positive even numbers less than twelve is",sum)

def sum_n(n):
    i=0
    total=0
    while i<=n:
        total=i+total
        i=i+1
    return total
print(sum_n(3))
