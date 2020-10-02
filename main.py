def reverse_bits(num):
  output = bin(num)
  output = output[2:len(output):1]
  while(len(output)<32):
    output = "0" + output
  output = output[::-1]
  return binaryToDecimal(output)

def binaryToDecimal(str):
  return int(str,2)

print(reverse_bits(5))