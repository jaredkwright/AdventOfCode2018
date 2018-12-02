input = open('./input.txt', 'r')
data = input.readlines()

frequency = 0
for frequency_change in data:
    try:
        change = int(frequency_change.rstrip())
        if change:
            frequency += change
    except:
        print('Bad value: {}'.format(repr(frequency_change)))

print('frequency: {}'.format(frequency))

