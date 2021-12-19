#You are given a list of  lowercase English letters. For a given integer , 
#you can select any  indices (assume -based indexing) with a uniform probability from the list.
#Find the probability that at least one of the  indices selected will contain the letter: ''.
'''Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints:
1<=N<=10
1<=K<=N

All the letters in the list are lowercase English letters.

Sample Input:
4 
a a c d
2

Sample Output:
0.8333

Explanation:
All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)

Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.
Hence, the answer is 5/6.'''

import itertools

n=int(input())
lst=input().split()                          #example list=[a a c d]
k=int(input())
index_range=[i+1 for i in range(n)]
lst_a_index=[]
for i in range(len(lst)):
    if lst[i]=='a':
        lst_a_index.append(i+1)

y=itertools.combinations(index_range,k)
x=(list(y))

count=0
for i in x:
    for j in i:
        if j in lst_a_index:
            count+=1
            break
            
print(count/len(x))

