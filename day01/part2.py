from sets import Set

input = open('./input.txt', 'r')
data = input.readlines()

frequency = 0
frequencies = Set([])
index = 0
numlines = len(data)
while True:
    if index >= numlines:
        index = 0
    frequency_change = data[index]
    try:
        change = int(frequency_change.rstrip())
        if change:
            frequency += change
            if frequency not in frequencies:
                frequencies.add(frequency)
            else:
                print('input sequence first reaches {} twice'.format(frequency))
                break
        index += 1
    except:
        print('Bad value: {}'.format(repr(frequency_change)))
        break

