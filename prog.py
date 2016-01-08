'''
We have a set of freight cars. We want to hook them together to get the chain of maximum length. Some freight cars have a unique front end, and some can have either end in front. Two freight cars can be joined together only if their coupling mechanisms are compatible

Each freight car is described by a string of uppercase letters. The front end is the end with the letter that comes first in the alphabet (if it starts and ends with the same letter, either end can be in front). Two words can be hooked together only if the two adjoining ends have the same letter.

If more than one chain of the longest length is possible, return the one that comes first alphabetically. Remember that the length of a freight car chain is the number of freight cars in it, not the number of letters

The returned string should be all the freight cars in the chain, starting at the front of the chain, concatenated with '-' showing the coupling between adjacent freight cars.

Constriants

- There can be up to 50 freight cars

- Each element of freight cars contains only uppercase letters ('A'-'Z').

- Each element of freight cars contains between 3 and 10 characters inclusive.

Input Explanation

Line 1: N

Line 2: 1st word

Line 3: 2nd word

...

Line N: Nth word

Sample Input 1:

5
BAD
CZD
DEF
AYB
AZC
Output:

AYB-BAD-DEF
Sample Input 2:

3
EBA
DAA
EXX
Output:

ABE-EXX

'''
from sys import stdin
n = int(raw_input("Number of Trucks:"))
truck_list = []
for i in range(int(n)):
	line = raw_input()
	truck_list.append(line)
	truck_list.append(line[::-1])
sorted_list = sorted(truck_list)
freight_chain = []
for i in range(len(sorted_list)):
	start = sorted_list[i]
	chain = []
	chain.append(start)
	for j in range(len(sorted_list)):
		if start != sorted_list[j] and start[::-1] != sorted_list[j] and start[-1] == sorted_list[j][0]:
			chain.append(sorted_list[j])
			start = sorted_list[j]
	if len(chain) > 1:
	   freight_chain.append(chain)
	if n ==1:
	   print chain
	   exit()
print '-'.join(freight_chain[0])