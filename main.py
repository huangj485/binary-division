import argparse
import division
 
 
# Initialize parser
parser = argparse.ArgumentParser(description = "Multiply A and B with Booth's Algorithm")

# Define args
parser.add_argument("-A", type=int, required=True, help = "dividend")
parser.add_argument("-B", type=int, required=True, help = "divisor")
parser.add_argument("--s", dest = "s", action='store_true', help = "flag to save instead of print to console")
 
# Read args
args = parser.parse_args()
A = args.A #multiplicand
B = args.B #multiplier

n = max([A.bit_length(), B.bit_length()])

value = division.div(A, B, n)

if args.s:
  f = open("saved.txt", "w")
  f.write(value)
  f.close()
else:
  print(value)



