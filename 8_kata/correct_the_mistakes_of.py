def correct(s):
  result = ''

  for char in s:
    if char == '0':
      result += 'O'

    elif char == '1':
      result += 'I'

    elif char == '5':
      result += 'S'

    else:
      result += char
  
  return result

print(correct('51NGAP0RE'))