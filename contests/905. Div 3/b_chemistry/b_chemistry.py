from itertools import permutations
#!/usr/bin/python3

def can_form_palindrome(s: str, k: int):
    # base case, no characters to be removed, just check if palindrome
    if k == 0:
        if s == s[::-1]:
            return "YES"
        else:
            return "NO"
    else:
        # looking for characters to remove
        for permutation in permutations(list(s), len(s) - k):
            if is_palindrome(permutation):
                return "YES"  
            else:
                continue
    return "NO"


def is_palindrome(s):
    return s == s[::-1]    
 

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        user_data = [int(x) for x in input().split()]
        n = user_data[0]
        k = user_data[1]
        s = input()
        print(can_form_palindrome(s, k))