
def triangle(h):
    def recurse(count):
        if count > 0:
            print('*' * count)
            count -= 1
            recurse(count)
    recurse(h)



triangle(3)
