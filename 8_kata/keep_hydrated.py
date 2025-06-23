import math

def litres(time):
  whole_hours= math.trunc(time)

  return math.floor(whole_hours * 0.5)

print(litres(3))