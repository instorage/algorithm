import sys

try:
  arg = int(sys.argv[1])
except IndexError:
  arg = 5

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print 'factorial of', arg, 'is',fact(arg)
