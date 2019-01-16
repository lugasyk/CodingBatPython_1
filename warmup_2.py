# string_times
def string_times(str, n):
  return str*n

# front_times
def front_times(str, n):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  result = ""
  for i in range(n):
    result = result + front
  return result

#string_bits
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result


# string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result


#last2
def last2(str):
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count

# array_count9
def array_count9(nums):
  return nums.count(9)

# array_front9
def array_front9(nums):
  return nums[:4].count(9) > 0


#