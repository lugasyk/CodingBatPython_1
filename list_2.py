# counts evens
def count_evens(nums):
  count = 0
  for n in nums:
    count -= n%2-1
  return count

# big diff
def big_diff(nums):
  return (max(nums) - min(nums))


# centered_average
def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  return sum(nums)/len(nums)

# sum13
def sum13(nums):
  nums += [0]
  return sum(n for i, n in enumerate(nums) if n != 13 and nums[i-1] != 13)

# sum67
def sum67(nums):
    ignore = False
    sum = 0
    for i in nums:
        if i == 6:
            ignore = True
        elif i == 7 and ignore:
            ignore = False
        elif not ignore:
            sum += i

    return sum

# has22
def has22(nums):
  for i in range(len(nums)-1):
    if (nums[i] == 2) and (nums[i+1] == 2):
      return True
  return False

# array123
def array123(nums):
  for i in range(0,len(nums)-2):
    if [1,2,3] == nums[i:i+3]:
      return True
  return False


# string_match
def string_match(a, b):
  shortlen = min(len(a), len(b))
  count = 0
  for i in range(shortlen-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if  a_sub == b_sub:
      count = count +1
  return count