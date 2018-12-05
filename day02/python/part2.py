inputs = open('../input.txt', 'r')
data = inputs.readlines()
total_lines = len(data)
winning_boxes = []


def hamming_distance(box_id_1, box_id_2):
    return sum(id1 != id2 for id1, id2 in zip(box_id_1, box_id_2))


for index in range(0, total_lines):
    box1 = data[index]
    if len(winning_boxes) > 0:
        break
    if index + 1 >= total_lines:
        break
    for index2 in range(index + 1, total_lines):
        box2 = data[index2]
        if hamming_distance(box1, box2) == 1:
            winning_boxes.extend([box1, box2])
            break


def common_character(characters):
    (x, y) = characters
    return x == y


def common_characters(boxes):
    [box_1, box_2] = boxes
    matching_tuples = filter(common_character, zip(box_1, box_2))
    matching_characters = [t[0] for t in matching_tuples]
    return ''.join(matching_characters)


print('common characters: {}'.format(common_characters(winning_boxes)))
