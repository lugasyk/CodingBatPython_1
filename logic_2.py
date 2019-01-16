# makebriks

def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal



# lone_sum

def lone_sum(a, b, c):
  if a != b and a !=c and b!=c:
    return (a + b + c)
  elif a == b and a ==c and b ==c:
    return 0
  elif a == b:
    return  c
  elif a == c:
    return b
  elif b == c:
    return a

#  or

def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c: sum += a
    if b != a and b != c: sum += b
    if c != a and c != b: sum += c

    return sum

# lucky_sum
def lucky_sum(a, b, c):
    if a == 13:
      return 0
    if b == 13:
      return a
    if c == 13:
      return a + b
    else:
      return a + b + c

# no_teen_sum
def no_teen_sum(a, b, c):
  nums = (a,b,c)
  return sum(fix_teen(n) for n in nums)

def fix_teen(n):
  return 0 if n not in (15,16) and 13 <= n <= 19 else n

# round sum
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(n):
    if n % 10 >= 5:
        return n + 10 - (n % 10)
    return n - (n % 10)

# close_far
def close_far(a, b, c):
  cond1 = abs(a-b) <= 1 and abs(b-c) >= 2 and abs(a-c) >= 2
  cond2 = abs(a-c) <= 1 and abs(b-c) >= 2 and abs(a-b) >= 2
  return cond1 or cond2

# make_chocolate

def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5

    if remainder <= small:
        return remainder
    return -1

