from list import List
from util import *

sequence = List()


with open('../input.txt', 'r') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        previous = sequence.peek()
        if previous and previous.value and is_polarized(previous.value, c):
            sequence.pop()
        else:
            sequence.push(c)

print('sequence length: {}'.format(len(sequence)))
