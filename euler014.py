#!/usr/bin/python

LIMIT = 1000000
steps = [0] * LIMIT
max_step = 0
max_step_pos = 0

for i in range(2, LIMIT):
    test = i
    n_steps = 0

    while test > 1:
        if test % 2 == 1:
            test = (3 * test) + 1
        else:
            test //= 2
        n_steps += 1
        if test < i:
            n_steps += steps[test]
            break

    if n_steps > max_step:
        max_step = n_steps
        max_step_pos = i
    steps[i] = n_steps

print(max_step_pos)
