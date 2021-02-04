x = input()
NUM_LETTERS = 26 #Can't import modules I'm using a web based grader/compiler
def SpyCoder(S, N):
   y = ""
   for i in S:
      if(i.isupper()):
         x = ord(i)
         x += N
         if x > ord('Z'):
            x -= NUM_LETTERS
         elif x < ord('A'):
            x += NUM_LETTERS
         y += chr(x)
      else:
         y += " "
   return y

def GoodnessFinder(S):
   y = 0
   for i in S:
      if i.isupper():
         x = ord(i)
         x -= ord('A')
         y += letterGoodness[x]
      else:
         y += 1
   return y

def GoodnessComparer(S):
   goodnesstocompare = GoodnessFinder(S)
   goodness = 0
   v = ''
   best_v = S
   for i in range(0, 26):
     v = SpyCoder(S, i)
     goodness = GoodnessFinder(v)
     if goodness > goodnesstocompare:
         best_v = v
         goodnesstocompare = goodness
   return best_v


print(GoodnessComparer(x))