def square_sum(numbers):
  sum = 0

  for number in numbers:
    sum += number * number
  
  return sum

print(square_sum([1,20]))