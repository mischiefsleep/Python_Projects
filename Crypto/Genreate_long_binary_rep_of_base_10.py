# Here are three ways of generating sequential binary strings of 
# arbitrary length.

# import require functions from certain packages.
import math 


def generate_binary_method_1(n):

  # 2^(n-1)  2^n - 1 inclusive
  bin_arr = range(0, int(math.pow(2,n)))
  bin_arr = [bin(i)[2:] for i in bin_arr]

  # Prepending 0's to binary strings
  max_len = len(max(bin_arr, key=len))
  bin_arr = [i.zfill(max_len) for i in bin_arr]

  return bin_arr

# Start from 0 and continually adding 1 to the binary string
# Ex: generate_binary_method_2(5)

var = generate_binary_method_1(5)
print(var)


def generate_binary_method_2(n):

  bin_arr = []
  bin_str = [0] * n

  for i in range(0, int(math.pow(2,n))):

    bin_arr.append("".join(map(str,bin_str))[::-1])
    bin_str[0] += 1

    # Iterate through entire array if there carrying
    for j in range(0, len(bin_str) - 1):

      if bin_str[j] == 2:
        bin_str[j] = 0
        bin_str[j+1] += 1
        continue

      else:
        break

    
  return bin_arr



var = generate_binary_method_2(5)
print(var)
# Recursive string generation
# Ex: generate_binary_method_3(5 , [])
def generate_binary_method_3(n, l):

  if n == 0:
    return l
  else:
    if len(l) == 0:
      return generate_binary_method_3(n-1, ["0", "1"])
    else:
      return generate_binary_method_3(n-1, [i + "0" for i in l] + [i + "1" for i in l])


var = generate_binary_method_3(5,[])
print(var)