import math
a=int(input())
jvb='prime'
for i in range(2,int(math.sqrt(a))+1):
    if (a%i)==0:
            jvb='not prime'
            break
print(jvb)
