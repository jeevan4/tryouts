'''Given english and math test scores of students as integer arrays, 
find the number of students who have composite score below average
'''

from sys import stdin 
#Read the input using stdin
input = int(stdin.readline())
if input == 2:
    math = [int(i) for i in stdin.readline().strip().split(',')]
    eng = [int(i) for i in stdin.readline().strip().split(',')]
    if len(math) != len(eng):
        exit()
        total = map(lambda x,y: x+y, math,eng)
        aggregate = sum(total)/float(len(math))
        print len(filter(lambda x: x<aggregate,total))