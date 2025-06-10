def triangle(height):
    if height > 0:
        triangle(height-1)
        print('*' * height)
