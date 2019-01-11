# first_last6
def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
      return True
    else:
      return False

# same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

# make_pi
def make_pi():
  pi = [3, 1, 4]
  return pi

# common_end
def common_end(a, b):
  if len(a) >=1 and len(b) >= 1 and (a[0] == b[0] or a[-1] == b[-1]):
    return True
  else:
    return False

# sum3
def sum3(nums):
  return sum(nums)

# rotate_left3
def rotate_left3(nums):
  return nums[1:] + nums[:1]

# reverse3
def reverse3(nums):
  return nums[::-1]

# max_end3
def max_end3(nums):
  return [nums[0]]*3 if nums[0] >= nums[-1] else [nums[-1]]*3

# sum2
def sum2(nums):
  return sum(nums[:2])

# middle_way
def middle_way(a, b):
 return [a[1], b[1]]


# make_ends
def make_ends(nums):
    return [ nums[0] , nums[-1] ]

# has23
def has23(nums):
  return 2 in nums or 3 in nums

