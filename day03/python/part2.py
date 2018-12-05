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


def apply_claim(fabric_matrix, offsets, claim_size, current_claim_id):
    (o_x, o_y) = offsets
    (width, height) = claim_size
    x_max = o_x + width
    y_max = o_y + height
    current_claim = np.full(claim_size, current_claim_id, dtype=int)
    existing_claims = np.unique(fabric_matrix[o_x:x_max, o_y:y_max].flatten())
    existing_claims = existing_claims[np.where(existing_claims > 0)]
    fabric_matrix[o_x:x_max, o_y:y_max] += current_claim
    return existing_claims


fabric = np.zeros((FABRIC_WIDTH, FABRIC_HEIGHT), dtype=int)

valid_claims = set()

for claim in data:
    claim_id, offset_coords, size = parse_claim(claim)
    valid_claims.add(claim_id)
    (min_x, min_y) = offset_coords
    (w, h) = size
    max_x = min_x + w
    max_y = min_y + h
    remove_claims = apply_claim(fabric, offset_coords, size, claim_id)
    if remove_claims.size > 0:
        valid_claims.remove(claim_id)
    for c in remove_claims.tolist():
        if c in valid_claims:
            valid_claims.remove(c)

if len(valid_claims) > 0:
    remaining_claim = valid_claims.pop()
    print('remaining set: {}'.format(remaining_claim))