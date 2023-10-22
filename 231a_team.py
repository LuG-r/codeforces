#!/usr/bin/python3

n = int(input())
team = []

solved_problems = 0
for i in range(n):
    problem = input()
    confidence = sum([int(x) for x in problem.split(" ")])
    if confidence >= 2:
        solved_problems += 1

print(solved_problems)