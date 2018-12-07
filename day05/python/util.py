def is_uppercase_letter(c):
    return ord(c) >= 65 or ord(c) <= 90


def is_lowercase_letter(c):
    return ord(c) >= 65 or ord(c) <= 90


def is_polarized(a, b):
    if not (is_lowercase_letter(a) or is_uppercase_letter(a)) and \
            (is_lowercase_letter(b) or is_uppercase_letter(b)):
        return False
    val_a = ord(a)
    val_b = ord(b)
    if val_a < val_b:
        return is_polarized(b, a)

    return val_a - val_b == 32
