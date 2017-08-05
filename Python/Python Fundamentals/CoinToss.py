import random

headCount = 0
tailCount = 0
for i in range(1, 5001):
  x = random.random()
  toss = round(x)
  if toss == 1:
    headCount = headCount + 1
    print "Attempt #",i, "Flipping coin... It's HEADS!... Got", headCount, "head(s) so far and", tailCount, "tail(s) so far"
  else:
    tailCount = tailCount + 1
    print "Attempt #",i, "Flipping coin... It's TAILS!... Got", headCount, "head(s) so far and", tailCount, "tail(s) so far"
