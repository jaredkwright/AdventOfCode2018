import numpy as np

FABRIC_WIDTH = 1000
FABRIC_HEIGHT = 1000

inputs = open('../input.txt', 'r')
data = inputs.readlines()


def parse_claim(current_claim):
    [raw_id, _, raw_offset, raw_dimensions] = current_claim.split(' ')
    claim_id = int(raw_id.lstrip('#'))
    [x_offset_raw, y_offset_raw] = raw_offset.rstrip(':').split(',')
    offsets = (int(x_offset_raw), int(y_offset_raw))
    [width_raw, height_raw] = raw_dimensions.split('x')
    claim_size = (int(width_raw), int(height_raw))
    return claim_id, offsets, claim_size


def apply_claim(fabric_matrix, offsets, claim_size):
    (o_x, o_y) = offsets
    (width, height) = claim_size
    current_claim = np.ones(claim_size, dtype=int)
    fabric_matrix[o_x:o_x+width, o_y:o_y+height] += current_claim


fabric = np.zeros((FABRIC_WIDTH, FABRIC_HEIGHT), dtype=int)

for claim in data:
    _, offset_coords, size = parse_claim(claim)
    apply_claim(fabric, offset_coords, size)

threshold_fabric = fabric >= 2

overlaps = np.count_nonzero(threshold_fabric)

print('overlapping squares: {}'.format(overlaps))