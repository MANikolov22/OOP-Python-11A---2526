"""list = [1,2,3,4,5]
    print(list[0])
    print(list[-1])
    print(list[::2])"""

"""names=[]
for i in range(5):
    names.append(input())
print(names[::-1])"""

"""numbers=[3,7,2,8,5,10,1]
min=numbers[0]
max=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] < min:
        min=numbers[i]
    if numbers[i] > max:
        max=numbers[i]
print(min,max)"""

"""matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for row in matrix:
    print(row)"""

list=[1,2,3,4,5,6,7,8,9.10,11,12,13,14,15,16,17,18,19,20]
evens = [x**2 for x in range(len(list))]