#!/usr/bin/python3

t = int(input())

multiset = []

for i in range(t):
    user_data = input().split()
    operation = user_data[0]
    l = int(user_data[1]) 
    r = int(user_data[2])
    s = {x for x in range(l, r + 1)}
    if operation == '+':
        multiset.append(s)
    elif operation == '-':
        try:
            multiset.remove(s)
        except:
            pass

    if len(multiset) >= 2:
        if len(set.intersection(*multiset)) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
