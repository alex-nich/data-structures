'''
This is my implementation to a coding question on GeeksforGeeks:
https://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/
'''

from collections import defaultdict

input = [3,4,7,1,2,9,8]

length = len(input)
sum  = 0
d = defaultdict(list)

for i in range(length):
    for j in range(length):
        if (i < j):
            sum = input[i] + input[j]
            indices = (i,j)
            d[sum].append(indices)

print("\nInput: {}".format(input))

for k,v in d.items():
    if len(v) > 1:
        print("\n\nThese pairs have the same sum [{}]: ".format(k), end=" ")
        
        for tuple in v:
            print("({},{}), ".format(input[tuple[0]], input[tuple[1]]),end = " ")