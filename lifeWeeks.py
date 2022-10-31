year = input("How old are you ? ")
live_left = int(90 - int(year))
dayleft = 365 * live_left
weeksleft = 52 * live_left 
monthleft = 12 * live_left

print(f"You have {dayleft} days, {weeksleft} weeks, and {monthleft} months left.")