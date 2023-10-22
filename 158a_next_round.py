#!/usr/bin/python3

nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])
k_index = k - 1

scores = [int(x) for x in input().split(" ")]

if scores[k_index] <= 0:
    print(0)
else:
    advancers = k
    for i in range(k_index + 1, len(scores)):
        if scores[i] >= scores[k_index]:
            advancers += 1
    print(advancers)
