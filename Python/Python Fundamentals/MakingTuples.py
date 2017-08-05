# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def tupleTups():
  aList = []
  tups = ()
  for key, data in my_dict.items():
    tup = ()
    tup =  key, data
    aList.append(tup)
  print aList
    
print tupleTups()