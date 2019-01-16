#double char
def double_char(str):
    return ''.join([char*2 for char in str])

#count hi
def count_hi(str):
  return str.count("hi")

#count cat and dog
def cat_dog(str):
  catcount = str.count("cat")
  dogcount = str.count("dog")
  if catcount == dogcount:
    return True
  else:
    return False

# count_code
def count_code(str):
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count

# end_other
def end_other(a, b):
  long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
  return long_s.lower().endswith(short_s.lower())

# end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))