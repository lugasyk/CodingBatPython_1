def monkey_troube(a_smile, b_smile):
    while True:
        if a_smile and b_smile:
            return True
        if not a_smile and not b_smile:
            return True
        return False