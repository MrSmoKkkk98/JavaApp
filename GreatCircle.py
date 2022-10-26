import math


def great_circle(x1, y1, x2, y2):
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)
    r = 6371.0
    sin_x = math.sin((x2-x1) / 2)
    sin_y = math.sin((y2-y1) / 2)
    pow_sin_x = math.pow(sin_x, 2)
    pow_sin_y = math.pow(sin_y, 2)
    formula_in_bracket = math.sqrt(
        pow_sin_x + math.cos(x1) * math.cos(x2) * pow_sin_y)
    formula = 2 * r * math.asin(formula_in_bracket)
    return f"{formula} kilometers"


print(great_circle(60.0, 15.0, 120.0, 105.0))
