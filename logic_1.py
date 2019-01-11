# cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend == False and abs(40) <= cigars <= abs(60) or (cigars >= 40 and is_weekend):
    return True
  else:
    return False

# date_fashion
def date_fashion(you, date):
  if you <=2 or date <= 2:
    return 0
  elif you < 8 and date < 8 :
    return 1
  else:
    return 2

# squirrel_play
def squirrel_play(temp, is_summer):
  if not is_summer and 60 <= temp <= 90:
    return True
  elif 60 <= temp <= 100 and is_summer:
    return True
  else:
    return False

# caught_speeding
def caught_speeding(speed, is_birthday):
  if not is_birthday and speed <= 60 or is_birthday and speed <= 65 :
    return 0
  elif not is_birthday and 60 < speed <= 80 or is_birthday and  65 < speed <= 85:
    return 1
  elif not is_birthday and  speed > 80 or is_birthday and speed > 85:
    return 2

# sorta_sum
def sorta_sum(a, b):
  if 10 <= (a + b) <=19:
   return 20
  else:
    return a+b

# alarm_clock
def alarm_clock(day, vacation):
  if vacation and day in (0,6):
    return "off"
  elif vacation or day in (0,6):
    return "10:00"
  else:
   return "7:00"


# alarm_clock
def alarm_clock(day, vacation):
  if vacation and day in (0,6):
    return "off"
  elif vacation or day in (0,6):
    return "10:00"
  else:
   return "7:00"

# love6
def love6(a, b):
  sum = a + b
  dif = abs(a - b)
  return 6 in (a, b, sum, dif)

# in1to10
def in1to10(n, outside_mode):
  if not outside_mode and n in range(1,11):
    return True
  elif outside_mode and (n <= 1 or n >= 10) :
    return True
  else:
    return False

# near_ten
def near_ten(num):
    dif = num % 10
    return 8 <= dif or 2 >= dif



