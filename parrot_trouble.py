def parrot_trouble(talking, hour)
    if talking and (7 > hour or hour > 20):
        return True
    else:
        return False