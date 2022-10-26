def isRightTriangle(a, b, c):
    if a and b and c >= 0:
        right_triangle = a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
        return right_triangle
    else:
        return False


print(isRightTriangle(0, 0, 0))
