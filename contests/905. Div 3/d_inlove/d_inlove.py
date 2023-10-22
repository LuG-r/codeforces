#!/usr/bin/python3

multiset = []

def update_multiset(operation: str, left: int, right: int) -> None:
    global multiset
    s = {x for x in range(left, right + 1)}
    if operation == '+':
        multiset.append(s)
    elif operation == '-':
        try:
            multiset.remove(s)
        except:
            pass



def calculate_intersection() -> str:
    global multiset
    if len(multiset) >= 2:
        if len(set.intersection(*multiset)) == 0:
            return "YES"
        else:
            return "NO"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        user_data = input().split()
        operation = user_data[0]
        l = int(user_data[1]) 
        r = int(user_data[2])
        
        update_multiset(operation, l, r)
        print(calculate_intersection())