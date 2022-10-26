def CMYKtoRGB(cyan=float, magenta=float, yellow=float, black=float):
    white = 1 - black
    red = 255 * (white) * (1 - cyan)
    green = 255 * (white) * (1 - magenta)
    blue = 255 * (white) * (1 - yellow)
    return f'''red = {round(red)}
green = {round(green)}
blue = {round(blue)}'''


print(CMYKtoRGB(1.0, 0.58, 0.0, 0.33))
