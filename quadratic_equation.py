from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        sqrt_discriminant = sqrt(discriminant)
        two_a = 2 * a

        root1 = (-b - sqrt_discriminant) / two_a
        if discriminant != 0:
            root2 = (-b + sqrt_discriminant) / two_a
        else:
            root2 = None
    else:
        root1, root2 = None, None

    return root1, root2

