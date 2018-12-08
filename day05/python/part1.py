from list import List
from util import *

sequence = List()


with open('../input.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        previous = sequence.peek()
        if previous and previous.value and is_polarized(previous.value, char):
            sequence.pop()
        else:
            sequence.push(char)

print('sequence length: {}'.format(len(sequence)))
