def sleep_in(weekday, vacation):
   #The parameter weekday is True if it is a weekday,
   # and the parameter vacation is True if we are on vacation.
   # We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in
   #1 version

    while True:
        if weekday is False and vacation is False:
            return True
        elif weekday is True and vacation is False:
            return False
        elif weekday is False or vacation is True:
            return True
#or


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
  # This can be shortened to: return(not weekday or vacation)
