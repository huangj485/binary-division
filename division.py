def flip(s): #flips bits
  if s == "0":
    return "1"
  else:
    return "0"

def div(A, B, n): #n is bit length
  nA = n
  nB = n

  toReturn = ""
  toReturn += "Divisor: " + str(A) + "\n"
  toReturn += "Dividend: " + str(B) + "\n"
  toReturn += "Number of Bits: " + str(n) + "\n"
  toReturn += "Actual Quotient: " + str(int(A/B)) + "\n"
  toReturn += "Actual Remainder: " + str(A - int(A/B) * B) + "\n"

  
  formatter = "{0:0" + str(nA + nB) + "b}" #define formatter

  #B = B

  R = A # Dividend

  spaceOffset = len(str(nB)) #for formatting output
  upperMask = 2**(2*n) - 2**(n)
  lowerMask = (2**n) - 1
  for x in range(nB+1):
    test = ((R & upperMask) >> n) - B

    if test >= 0: 
      R = (test << n) + (R & lowerMask) 
      R = R << 1 
      R += 1
    else:
      R = R << 1
    
    temp = R
    toPrint = str(formatter.format(temp))
    s = str(toPrint)
    
    if R < 0:
      temp = map(flip, s)
      temp = "".join(temp)
      news = formatter.format(int(temp, 2) + 1)
      toPrint = news

    spaceUnOffset = len(str(x))
    toReturn += "Pass " + str(x) + ((spaceOffset - spaceUnOffset) * " ") + " -- Binary R: " + toPrint + " -- Actual R: " + str(R) + "\n"

  mask = 2**n - 1
  quotient = R & mask
  remainder = R >> (n+1)

  toReturn += "Quotient: " + str(quotient) + "\n"
  toReturn += "Remainder: " + str(remainder)
  return toReturn

