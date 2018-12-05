inputs = open('../input.txt', 'r')
data = inputs.readlines()


twos = 0
threes = 0

for line in data:
    box_id = line.rstrip()
    characters = {}
    for character in box_id:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    has_two = has_three = False

    for character, count in characters.items():
        if has_two and has_three:
            break
        if not has_three and count == 3:
            has_three = True
        if not has_two and count == 2:
            has_two = True

    if has_two:
        twos += 1
    if has_three:
        threes += 1

checksum = twos * threes

print('checksum: {}'.format(checksum))
