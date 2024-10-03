#Logical Operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be tru
#                    and = both conditions must be tru
#                    not = inverts the conditions (not false, not true)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The event is still scheduled")
