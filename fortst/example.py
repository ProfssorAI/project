x , y = 0 , 0
array = []
def ispalindrom(a):
    if a == a[::-1]:
        return True
    else:
        return False

for i in range(100 , 1000):
    for j in range(100,1000):
        number = i*j
        if ispalindrom(str(number)):
            array.append(number)
print(max(array))

