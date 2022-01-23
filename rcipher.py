def rotationalCipher(input, rotation_factor):
  # Write your code here
  capA = ord('A')
  capZ = ord('Z')
  smallA = ord('a')
  smallZ = ord('z')
  output = ''
  print(input, rotation_factor)
  for i in input:
    if i.isnumeric():
      newval = int(i)+ rotation_factor % 10
      if newval >9:
        val = str(newval % 10)
      else:
        val = str(newval)
    elif i.isalpha():
      if i.isupper():
        newval = ord(i) + rotation_factor %26
        if newval > capZ:
          val = chr(capA-1 + (newval % capZ))
        else:
          val = chr(newval)
      else:
        newval = ord(i) + rotation_factor%26
        if newval > smallZ:
          val = chr(smallA-1 + (newval % smallZ))
        else:
          val = chr(newval)
    else:
      val = i
    output += val
  return output
