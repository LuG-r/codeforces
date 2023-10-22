#!/usr/bin/python3

def minimum_seconds_required(pin_digits: list) -> int:
    total = 0
    position = 0
    pad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for digit in pin_digits:
        while digit != pad[position]:
            total += 1
            if digit == 0:              # if looking for 0, always go right
                position += 1
            elif pad[position] == 0:    # if on 0, always go left
                position -= 1
            else:
                if digit < pad[position]:
                    position -= 1
                else:
                    position += 1
        else:
            total += 1
    return total

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pin_digits = [int(x) for x in input()]
        print(minimum_seconds_required(pin_digits))