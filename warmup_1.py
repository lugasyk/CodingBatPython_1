# 1 sleep_in
def sleep_in(weekday, vacation):
    while True:
        if weekday is False and vacation is False:
            return True
        elif weekday is True and vacation is False:
            return False
        elif weekday is False or vacation is True:
            return True

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
    while True:
        if a_smile and b_smile:
            return True
        if not a_smile and not b_smile:
            return True
        return False

    # if not a_smile or b_smile:
    # return True
    # else:
    # return False

# sum_double
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

# diif21
def diff21(n):
  if n > 21:
    return (n - 21) * 2
  else:
    return 21 - n

# parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (7 > hour or hour > 20):
    return True
  else:
    return False

# makes10
def makes10(a, b):
  if a + b == 10 or a == 10 or b == 10:
    return True
  else:
    return False

# near_hundred
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return((a < 0 and b > 0) or (a > 0 and b < 0))

# not_string
def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str

# missing_char
def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

# front_back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

# front3
def front3(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front

